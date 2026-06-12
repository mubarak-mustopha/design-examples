import sys

def find_duplicates(filenames):
    matches = []
    for left in filenames:
        for right in filenames:
            if same_bytes(left, right):
                matches.append((left, right))
    return matches

def same_bytes(afile, bfile):
    a_bytes = open(afile, "rb").read()
    b_bytes = open(bfile, "rb").read()
    return a_bytes == b_bytes

if __name__=="__main__":
    duplicates = find_duplicates(sys.argv[1:])
    for left, right in duplicates:
        print(left, right)
