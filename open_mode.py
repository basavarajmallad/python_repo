import os
with open("file2", "w") as fh:
   fh.write("wellcome to the devops\n")
   fh.write("file created")
def fnc_file(file):
    if os.path.isfile(file):
        with open(file, "r") as fh:
            content=fh.read()
            #print(content)
        return(content)
    else:
        print("file does not exist")
        return("no_content")


filename=input("enter file name")
display=fnc_file(filename)
print(display)


