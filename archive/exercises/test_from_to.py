from pathlib import Path
from unittest.mock import patch
import pytest
import os

from hash_all import hash_all
from backup import backup
from from_to import restore

STATE_A = {"a.txt": "aaa", "b.txt": "bbb", "sub_dir/c.txt": "ccc"}
STATE_B = STATE_A | {"b.txt": "bb$", "sub_dir/d.txt": "ddd"}
STATE_C = STATE_B.copy()
STATE_C.pop("b.txt")


SOURCE_DIR = "sample_dir"
BACKUP_DIR = "/backup"
MANIFEST_FILENAMES = ["1000.csv", "1001.csv", "1002.csv"]

def mockHash(byte_data: bytes):
    return byte_data.decode()[:3]

@pytest.fixture
def our_fs(fs):
    #  state A
    for filename, contents in STATE_A.items():
        fs.create_file(f"{SOURCE_DIR}/{filename}", contents=contents)

    with patch("hash_all.ourHash", side_effect=mockHash), \
            patch("backup.current_time", return_value=1000):
        backup(SOURCE_DIR, BACKUP_DIR)

    # state B
    with open(f"{SOURCE_DIR}/b.txt", "w") as f:
        f.write("bb$")

    with open(f"{SOURCE_DIR}/sub_dir/d.txt", "w") as f:
        f.write("ddd")

    with patch("hash_all.ourHash", side_effect=mockHash), \
            patch("backup.current_time", return_value=1001):
        backup(SOURCE_DIR, BACKUP_DIR)

    # state C
    os.remove(f"{SOURCE_DIR}/b.txt")
    with patch("hash_all.ourHash", side_effect=mockHash), \
            patch("backup.current_time", return_value=1002):
        backup(SOURCE_DIR, BACKUP_DIR)

def test_fs(our_fs):
    assert Path(SOURCE_DIR).exists()
    assert Path(BACKUP_DIR).exists()
    for filename in STATE_C:
        assert Path(SOURCE_DIR, filename).exists()

    all_hashes = set()
    for state in [STATE_A, STATE_B, STATE_C]:
        all_hashes |= set(state.values())

    for hash in all_hashes:
        assert Path(BACKUP_DIR, f"{hash}.bck").exists()

    for man in MANIFEST_FILENAMES:
        assert Path(BACKUP_DIR, man).exists()

def test_from_c_to_a(our_fs):
    with patch("hash_all.ourHash", side_effect=mockHash):
        assert dict(hash_all(SOURCE_DIR)) == STATE_C
        restore(f"{BACKUP_DIR}/1000.csv", SOURCE_DIR, BACKUP_DIR)
        assert dict(hash_all(SOURCE_DIR)) == STATE_A    
    