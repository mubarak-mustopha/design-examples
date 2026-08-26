from pathlib import Path
import pytest

from hash_all import hash_all, HASH_LEN

@pytest.fixture
def our_fs(fs):
    fs.create_file("a.txt", contents="aaa")
    fs.create_file("b.txt", contents="bbb")
    fs.create_file("sub_dir/c.txt", contents="ccc")

def test_hashing(our_fs):
    result = hash_all(".")
    expected = {"a.txt", "b.txt", "sub_dir/c.txt"}
    assert {r[0] for r in result} == expected
    assert all(len(r[1]) == HASH_LEN for r in result)

def test_change(our_fs):
    result = hash_all(".")
    old = [r for r in result if r[0] == "a.txt"][0]
    assert old[0] == "a.txt"
    with open("a.txt", "w") as writer:
        writer.write("The content of a.txt changed!!")
    result = hash_all(".")
    new = [r for r in result if r[0] == "a.txt"][0]
    assert new[0] == "a.txt" and new != old
    