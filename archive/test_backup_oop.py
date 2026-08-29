from pathlib import Path
from unittest.mock import patch
from unittest.mock import patch
import pytest

from backup_oop import ArchiveLocal


FILES = {"a.txt": "aaa", "b.txt": "bbb", "sub_dir/c.txt": "ccc"}

@pytest.fixture
def our_fs(fs):
    for filename, contents in FILES.items():
        fs.create_file(filename, contents=contents)

def test_nested_example(our_fs):
    timestamp = 1234
    backup_dir = "/backup"
    local_archive = ArchiveLocal(".", backup_dir)
    
    with patch("backup_oop.current_time", return_value=timestamp):
        manifest = local_archive.backup()
    assert Path(f"{backup_dir}/{timestamp}.csv").exists(), "Manifest not created"
    for filename, hashcode in manifest:
        assert Path(f"{backup_dir}/{hashcode}.bck").exists(), f"Did not backup {filename}"
