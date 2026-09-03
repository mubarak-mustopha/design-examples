from pathlib import Path
import argparse
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

class SequentialArchiveLocal(ArchiveLocal):
    def __init__(self, source_dir, backup_dir, manifest_counter_path=None):
        super().__init__(source_dir, backup_dir)
        self._manifest_counter_path = manifest_counter_path or f"{self._backup_dir}/manifest_counter"

    def _write_manifest(self, manifest):
        dest_path = Path(self._backup_dir)
        if not dest_path.exists():
            dest_path.mkdir()

        manifest_counter = Path(self._manifest_counter_path)
        if not manifest_counter.exists():
            manifest_counter.write_text("00000000")

        manifest_number = int(manifest_counter.read_text()) + 1
        manifest_name = str(manifest_number).zfill(8) + ".csv"   

        with open(f"{self._backup_dir}/{manifest_name}", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["filename", "hashcode"])
            writer.writerows(manifest)

        manifest_counter.write_text(str(manifest_number).zfill(8))   

if __name__=="__main__":
    parser = argparse.ArgumentParser(usage="python backup.py src_dir backup_dir -s [manifest-counter-path]")
    parser.add_argument("source_dir")
    parser.add_argument("backup_dir")
    parser.add_argument("-s", "--seq", const="default", nargs="?", default=None)

    args = parser.parse_args()
    if args.seq is None:
        archiver = ArchiveLocal(args.source_dir, args.backup_dir)
    elif args.seq == "default":
        archiver = SequentialArchiveLocal(args.source_dir, args.backup_dir)
    else:
        archiver = SequentialArchiveLocal(args.source_dir, args.backup_dir, args.seq)

    archiver.backup()