import os
print(os.getcwd())
os.makedirs("dir12", exist_ok=True)
print("list all files")
print(os.listdir())
files = os.listdir()
for file in files:
    #print(file)
    if file.endswith(".py"):
        print(file)
os.chdir("/home/ubuntu/dir12")
print(os.getcwd())
print(os.listdir())
print(os.path.basename("/home/ubuntu/dir12"))
print("check")
print(os.path.exists("/home/ubuntu/dir121"))
print("------")
for root, dirs, files in os.walk("/home/ubuntu"):
    print(root)
    print(dirs)
    print(files)

