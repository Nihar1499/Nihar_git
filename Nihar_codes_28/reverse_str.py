str1=input("Please provide a string-")
str2=""
for i in range(len(str1)-1,-1,-1):
    str2=str2+str1[i]
print(str2)