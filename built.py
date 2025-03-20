str1 = "Devops Engnieer"
strlower = str1.lower()
print(strlower)
strupper = strlower.upper()
print(strupper)

if str1.lower().startswith("dev"):
    print("it start with pattern")
else:
    print("statment is not start with pattern")
if str1.lower().endswith("dev"):
    print("statement ends with dev")
else:
    print("statement is not ends with dev")

str2 = "devops sre release"
strreplace = str2.replace(" ", "|")
print(strreplace)

str3 = "devops,sre,release" 
val1, val2 = str3.split(",", 1)
val101, val201, val301= str3.split(",", 2)
print(val101, val201, val301)
val1, val2 = str3.rsplit(",", 1)
print(val1, val2)
