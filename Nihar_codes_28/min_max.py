l1=[20,30,10,40]
#sorting the list in ascending order
for i in range(len(l1)):
    for j in range(len(l1)):
        if l1[i]<l1[j]:
            temp=l1[j]
            l1[j]=l1[i]
            l1[i]=temp
print(l1)
min=l1[0]
max=l1[len(l1)-1]
print(f'min={min}')
print(f'max={max}')