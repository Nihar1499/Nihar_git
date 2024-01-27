str1 = "3G4C"
str2=""
for i in range(len(str1)):
	if i%2==0:
		cnt=int(str1[i])
		for n in range(cnt):
			#print(str1[i+1])
			str2=str2+str1[i+1]
print(str2)
