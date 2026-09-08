from glob import glob
from hashlib import sha256
from pathlib import Path
import sys

HASH_LEN =16

def hash_all(root):
    result = []
    for name in glob("**/*.*", root_dir=root, recursive=True):
        full_name = Path(root, name)
        with open(full_name, "rb") as f:
            hash_code = ourHash(f.read())
            result.append((name, hash_code))
    return result

def ourHash(byte_stream: bytes):
    return sha256(byte_stream).hexdigest()[:HASH_LEN]

if __name__=="__main__":
    assert len(sys.argv) == 2, "Usage: python hash_all.py sample_dir"
    result = hash_all(sys.argv[1])
    print("filename", "hash")
    for filename, hash in result:
        print(filename, hash)
