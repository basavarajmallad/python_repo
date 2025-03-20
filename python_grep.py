import re
import sys
import os
emaildata="basavarajmallad <basavaramallad@gmail.com>, devaraj <devaraj@gmail.com>, sarath123 <sarath123@gmail.com>, basavaraj <basavaraj@gmail.com>"
result=re.search(r"basavaraj",emaildata)
print(result)
result=re.findall(r"devaraj", emaildata)
print(result)
result=re.search(r"Sarath" ,emaildata,re.IGNORECASE)
print(result)
result=re.search(r"sara[t, h]", emaildata)
print(result)
result=re.search(r"sara[a-z]", emaildata)
print(result)
result=re.search(r"sar[a-z]+", emaildata)
print(result)
result=re.search(r"\w+@\w+\.\w+", emaildata)
print(result)
result1=sys.argv[0],sys.argv[1],sys.argv[2]
print(result1)
