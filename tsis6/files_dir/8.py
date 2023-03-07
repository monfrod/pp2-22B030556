import os

file_path = '/Users/yunus/Documents/GitHub/pp2-22B030556/tsis6/files_dir/my_list.txt'

if os.path.exists(file_path):
    if os.access(file_path, os.R_OK) and os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"{file_path} deleted successfully.")
    else:
        print(f"{file_path} is not accessible for read and write.")
else:
    print(f"{file_path} does not exist.")
