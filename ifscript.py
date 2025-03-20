var1 = 50
var2 = 60
var3 = 15
#----if elase ----
if var1 >  var2 :
    print(var1, " is greater than ", var2)
else:
    print(var2, " is greater than ", var1)

#---- nested if ----
if var1 > var2 and var1 >var3:
    print(var1, " is greatest among all the numbers")
elif var2 > var3:
    print(var2, "is greatest among all the  numbers")
else:
    print(var3, "is greatest among all the numbers")

mylist = [ "basavaraj", "kushi", "pooja"]
 
if "kushi" in mylist:
    print("kushi is found")
else:
    print("not found")

if "kushi" not in mylist:
    print("kushi is not present")

if mylist:
    print("list  has values")
else:
    print("my list is empty")
    
mylist1 = []    
if not mylist1:
    print("list is empty")

mydict = {
            "name" : "basavaraj",
            "role" : "developer"
         }
if "id" in mydict:
    print("key found")
else:
    print("key not found")
 
if "basavaraj" in mydict.values():
    print("basavaraj is present in dictnory")
else:
    print("basavaraj not present in dictnory")

if mydict["name"] == "basavaraj":
    print("present")
