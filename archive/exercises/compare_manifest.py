import csv
import sys

def compare_manifests(manifest_file1, manifest_file2):
    manifest1 = read_manifest(manifest_file1)
    manifest2 = read_manifest(manifest_file2)

    filenames = {f for f in list(manifest1) + list(manifest2)}
    files_history = {
        filename: (manifest1.get(filename), manifest2.get(filename))
        for filename in filenames
    }

    categories = categorize_files(files_history)

    print_categories(categories)

def categorize_files(files_history):
    categories = {"changed": set(),"renamed": set(), "deleted": set(), "added": set()}

    for filename, hashes in files_history.items():
        if hashes[0] is None:
            categories["added"].add(filename)
        elif hashes[1] is None:
            categories["deleted"].add(filename)
        elif hashes[0] != hashes[1]:
            categories["changed"].add(filename)

    if categories["added"] and categories["deleted"]:
        renamed = get_renamed_files(categories["deleted"].copy(), categories["added"].copy(), files_history)
        if renamed:
            categories["renamed"] = renamed
            for old, new in renamed:
                categories["deleted"].remove(old)
                categories["added"].remove(new)
    return categories

def get_renamed_files(deleted_files: set, added_files: set, files_history):
    renamed = set()
    added_file_hashes = {files_history[new][1]: new for new in added_files}

    for deleted in deleted_files:
        deleted_hash = files_history[deleted][0]
        new_file = added_file_hashes.get(deleted_hash)
        if new_file:
            renamed.add((deleted, new_file))

    return renamed

def print_categories(categories):
    print(format_categories(categories))

def format_categories(categories):
    result = []
    for cat in categories:
        header = f"{cat} files"
        marker = "-" * len(header)
        if cat == "renamed":
            files = {f"{old} -> {new}" for old, new in categories[cat]}
        else:
            files = categories[cat]
        if len(files) == 0:
            files = ["None"]
        result.append(f"{header}\n{marker}\n" + "\n".join(files))

    return "\n\n".join(result)
        
 
def read_manifest(manifest_file):
    with open(manifest_file, "r") as file:
        reader = csv.reader(file)
        # skip header
        next(reader) 
        return dict(reader)

if __name__=="__main__":
    assert len(sys.argv) == 3, "Usage: python compare-manifest.py man1.csv man2.csv"
    compare_manifests(sys.argv[1], sys.argv[2])