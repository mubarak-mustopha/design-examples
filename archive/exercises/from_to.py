import os
import shutil
import sys

from compare_manifest import categorize_files, read_manifest
from hash_all import hash_all

def restore(manifest_file, target_dir, backup_dir):
    from_manifest = dict(hash_all(target_dir))
    to_manifest = read_manifest(manifest_file)

    filenames = {f for f in list(from_manifest) + list(to_manifest)}
    files_history = {
        filename: (from_manifest.get(filename), to_manifest.get(filename))
        for filename in filenames
    }

    categories = categorize_files(files_history)

    restore_files(list(categories["added"]) + list(categories["changed"]), to_manifest, backup_dir, target_dir)
    rename_files(categories["renamed"], target_dir)
    delete_files(categories["deleted"], target_dir)
    
def restore_files(filenames, manifest, backup_dir, target_dir):
    for filename in filenames:
        hash = manifest[filename]
        shutil.copy(f"{backup_dir}/{hash}.bck", f"{target_dir}/{filename}")


def rename_files(filenames, target_dir):
    for old, new in filenames:
        os.rename(f"{target_dir}/{old}", f"{target_dir}/{new}")

def delete_files(filenames, target_dir):
    for filename in filenames:
        os.remove(f"{target_dir}/{filename}")

if __name__=="__main__":
    assert len(sys.argv) == 4, "Usage: python from_to.py manifest_file target_dir backup_dir"
    restore(sys.argv[1], sys.argv[2], sys.argv[3])