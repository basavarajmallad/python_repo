print("Hello, World!")
str1 = "BASAVARAJ"
str2 = "MALLAD"
result = str1 + " " + str2
print(result)
#---- length of string ---
#text = "Python is awesome"
text = result
length = len(text)
print("Length of the string:", length)
#----- lowercase and uppercase ----
text = "Python is awesome"
uppercase = text.upper()
lowercase = text.lower()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
#------ replace function ---
text = "Python is awesome"
new_text = text.replace("awesome", "great")
print("Modified text:", new_text)
#------split function ---
text = "basavaraj mallad sarat devaaraj vinay"
words = text.split()
print("Words:", words)
#-------strip function -------
text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)
print("length of string before strip: ", len(text))
print("lenfthe of the string after strip: ", len(stripped_text))
#--------substring function-------
text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")
