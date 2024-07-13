import os

def find_junk_files(directory, extensions):
    junk_files = []
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extensions):
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                junk_files.append(file_path)  # Hanya path file yang ditambahkan ke list junk_files
                total_size += file_size
    return junk_files, total_size

def delete_files(file_paths):
    for file_path in file_paths:
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Failed to delete: {file_path} - {e}")

def main():
    storage_path = "/storage/emulated/0"
    junk_extensions = ('.log', '.tmp', '.bak', '.old', '.swp', '.temp')
    junk_files, total_size = find_junk_files(storage_path, junk_extensions)
    if junk_files:
        print("Found junk files:")
        for junk_file in junk_files:
            print(junk_file)
        print(f"\nTotal size of junk files: {total_size / (1024 * 1024):.2f} MB")
    else:
        print("No junk files found.")

    
    delete_files(junk_files)

if __name__ == "__main__":
    main()