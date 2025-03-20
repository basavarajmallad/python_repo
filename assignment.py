import os
import sys
import re
import argparse

#reading the arguments  from command line 
parser=argparse.ArgumentParser(description="python based command to read file")
parser.add_argument("filename", help="it is the name file to write data in file")
args=parser.parse_args()
dest_file = args.filename

with open(dest_file, "w") as fp1:
    fp1.write("")

def fnc_search_pattern():
    with open(dest_file, "a") as fp2:
        for root, dirs, files in os.walk("/home/ubuntu/spring-framework"):
            for file in files:
                if file.endswith(".java"):
                    filepath=os.path.join(root, file)
                    with open(filepath, "r") as fp3:
                        for line in fp3:
                            if re.search(r"copyright", line, re.IGNORECASE):
                                fp2.write(line)


fnc_search_pattern()
