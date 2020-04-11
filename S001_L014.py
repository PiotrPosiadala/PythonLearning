import os

files_to_process = [
    r".\S001_L014a.py",
    r".\S001_L014b.py"
    ]

for file_path in files_to_process:
 
    with open(file_path, 'r') as f:
        print("File {} ...".format(os.path.basename(file_path)))
        source = f.read()
        exec(source)
