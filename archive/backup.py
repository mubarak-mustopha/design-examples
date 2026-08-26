from pathlib import Path
import csv
import shutil
import sys
import time

from hash_all import hash_all

def backup(source_dir, dest_dir):
    manifest = hash_all(source_dir)
    timestamp = current_time()
    write_manifest(manifest, timestamp,dest_dir)
    copy_files(manifest, source_dir, dest_dir)
    return manifest

def write_manifest(manifest, timestamp, dest_dir):
    dest_path = Path(dest_dir)
    if not dest_path.exists():
        dest_path.mkdir()
    with open(f"{dest_dir}/{timestamp}.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["filename", "hashcode"])
        writer.writerows(manifest)

def copy_files(manifest, source_dir, dest_dir):
    for filename, hash_code in manifest:
        source_path = Path(source_dir, filename)
        dest_path = Path(dest_dir, f"{hash_code}.bck")
        if not dest_path.exists():
            shutil.copy(source_path, dest_path)

def current_time():
    return f"{time.time()}".split(".")[0]

if __name__ == "__main__":
    assert len(sys.argv) == 3, "Usage: python backup.py src_dir backup_dir"
    backup(sys.argv[1], sys.argv[2])