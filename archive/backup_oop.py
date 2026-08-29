from pathlib import Path
import csv
import shutil

from backup import current_time
from hash_all import hash_all

class Archive:
    def __init__(self, source_dir):
        self._source_dir = source_dir

    def backup(self):
        manifest = hash_all(self._source_dir)
        self._write_manifest(manifest)
        self._copy_files(manifest)
        return manifest

class ArchiveLocal(Archive):
    def __init__(self, source_dir, backup_dir):
        super().__init__(source_dir)
        self._backup_dir = backup_dir

    def _write_manifest(self, manifest):
        dest_path = Path(self._backup_dir)
        timestamp = current_time()
        if not dest_path.exists():
            dest_path.mkdir()
        with open(f"{self._backup_dir}/{timestamp}.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["filename", "hashcode"])
            writer.writerows(manifest)

    def _copy_files(self, manifest):
        for filename, hash_code in manifest:
            source_path = Path(self._source_dir, filename)
            dest_path = Path(self._backup_dir, f"{hash_code}.bck")
            if not dest_path.exists():
                shutil.copy(source_path, dest_path)