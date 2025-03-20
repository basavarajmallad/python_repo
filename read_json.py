import json
import sys

def process_json():
    file_name=input("enter the json file to read")
    with open(file_name, "r") as fh:
        json_content=json.load(fh)
        for ele in json_content:
           # print(ele)
            for key, val in ele.items():
                if key == "Source URL":
                    print(key,  val)
                    sys.exit(0)


        
if __name__ == "__main__":
    process_json()

