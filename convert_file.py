import argparse
import pandas as pd
def convert_excel_json(efile, jfile):
    df=pd.read_excel(efile, sheet_name="Sheet1")
    df_strip=df.map(lambda x: x.strip() if isinstance(x, str) else x)
    df_strip.to_json(jfile, orient='records', indent=4)
    print("excel file was converted to json file sucessfully")

subparse=argparse.ArgumentParser(description="arguments for converting the file excel to JSON")
subparse.add_argument("excel_file", help="provide the name of the excel file")
subparse.add_argument("json_file", help="provide the name of the json file")
args=subparse.parse_args()
convert_excel_json(args.excel_file, args.json_file)

