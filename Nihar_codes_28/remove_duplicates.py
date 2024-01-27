a = [10,10,20,20,30,40,50,50,50]
a.sort()
print(a)
l2=[]
cnt=0
length=len(a)
for i in range(length-1):
    #for the last digit
    if i+1==length-1:
        if a[i+1]==a[i]:
            #print(a[i+1])
            l2.append(a[i+1])
        else:
            #print(a[i+1])
            l2.append(a[i+1])
    #for num before last digit
    if a[i]==a[i+1]:
        continue
    else:
        #print(a[i])  
        l2.append(a[i])
print(l2)
#using set   
set1 = {a[0]}
for num in a:
    set1.add(num)
print(sorted(set1))
