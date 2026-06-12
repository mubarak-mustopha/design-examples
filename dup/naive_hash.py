import sys

def find_duplicates(filenames):
    matches = []
    for i_left in range(len(filenames)):
        left = filenames[i_left]
        for i_right in range(i_left):
            right = filenames[i_right]
            if same_bytes(left, right):
                matches.append((left, right))
    return matches

def same_bytes(afile, bfile):
    a_bytes = open(afile, "rb").read()
    b_bytes = open(bfile, "rb").read()
    return a_bytes == b_bytes

def find_groups(filenames):
    groups = {}
    for fn in filenames:
        file_bytes = open(fn, "rb").read()
        file_hash = naive_hash(file_bytes)
        if file_hash not in groups:
            groups[file_hash] = set()
        groups[file_hash].add(fn)

    return groups

def naive_hash(content_bytes):
    return sum(content_bytes) % 13

if __name__=="__main__":
    groups = find_groups(sys.argv[1:])
    for grp in groups.values():
        dups = find_duplicates(list(grp))
        for left, right in dups:
            print(left, right)
