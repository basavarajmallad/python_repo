import os
def file_search():
    for root, dirs, files in os.walk("/home/ubuntu"):
        for file in files:
            if file.endswith(".py"):
                print(file, root)


file_search()
