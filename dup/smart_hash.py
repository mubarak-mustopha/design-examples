from hashlib import sha256
import sys

def find_groups(filenames):
    groups = {}
    for fn in filenames:
        data = open(fn, "rb").read()
        hashcode = sha256(data).hexdigest()
        if hashcode not in groups:
            groups[hashcode] = set()
        groups[hashcode].add(fn)

    return groups

def naive_hash(content_bytes):
    return sum(content_bytes) % 13

if __name__=="__main__":
    groups = find_groups(sys.argv[1:])
    for grp in groups.values():
        print(", ".join(list(grp)))
