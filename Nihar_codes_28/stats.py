#Write a program to compute mean, median and mode without using the in-built python functions
l1=[2,2,3,4,5,5]
sum=0
#code for mean
for num in l1:
    sum=sum+num
mean=(sum/len(l1))
print(f'mean={mean}')

#code for median
for i in range(len(l1)):
    for j in range(len(l1)):
        if l1[i]<l1[j]:
            temp=l1[j]
            l1[j]=l1[i]
            l1[i]=temp
if len(l1)%2==0:
    f1=int(len(l1)/2)
    f2=f1+1
    median=(l1[f1-1]+l1[f2-1])/2
    print(f'median={median}')
elif len(l1)%2!=0:
    f1=int(len(l1)/2)
    median=l1[f1]
    print(f'median={median}')

#find mode
list1=[1,3,2,2,2,3,4,5,5,5]
list1.sort()
num_list=[]
cnt_list=[]
cnt=1
cnt2=1
#To get set of unique numbers and their count
for i in range (len(list1)-1):
    if i+1==len(list1)-1:
        if list1[i+1]==list1[i]:
            #print(list1[i+1])
            cnt2+=1
            #print(f'cnt={cnt2}')
            num_list.append(list1[i+1])
            cnt_list.append(cnt2)
        elif list1[i+1]!=list1[i]:
            #print(list1[i+1])
            cnt2=1
            #print(f'cnt={cnt2}')
            num_list.append(list1[i+1])
            cnt_list.append(cnt2)

    if list1[i]==list1[i+1]:
        cnt+=1
    else:
       #print(list1[i])
       #print(f'cnt={cnt}')
       num_list.append(list1[i])
       cnt_list.append(cnt)
       cnt=1
    if list1[i]==list1[len(list1)-1]:
        cnt2+=1
#print(num_list)
#print(cnt_list)

#to sort the cnt_list and subsequently the num_list
for n in range(len(cnt_list)):
    for m in range(len(cnt_list)):
        if cnt_list[n]>cnt_list[m]:
            t1=cnt_list[m]
            t2=num_list[m]
            cnt_list[m]=cnt_list[n]
            num_list[m]=num_list[n]
            cnt_list[n]=t1
            num_list[n]=t2
print(f'num list={num_list}')
print(f'countt list={cnt_list}')
cnt_max=cnt_list[0]
for i1 in range(len(cnt_list)):
    if cnt_list[i1]==cnt_max:
        print(f'mode={num_list[i1]}, repeated={cnt_list[i1]} times')