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

if __name__=="__main__":
    duplicates = find_duplicates(sys.argv[1:])
    for left, right in duplicates:
        print(left, right)
