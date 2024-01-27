str1="AATTGCTTGGCCC"
print(str1)
#counter for chara other than the last character
cnt=1
#counter for the last chara
cnt2=1
str2=""

for i in range(len(str1)-1):
    
    if str1[i]==str1[i+1]:
        cnt+=1
    else:
        print(f'chara={str1[i]} and cnt={cnt}')
        str2=str2+str1[i]
        str2=str2+str(cnt)
        cnt=1
        cnt2=1
    #code for the last character
    if i+1==len(str1)-1:
        if str1[i+1]==str1[i]:
            cnt2+=1
            print(f'chara={str1[i+1]} and cnt={cnt2}')
            str2=str2+str1[i+1]
            str2=str2+str(cnt2)
        elif str1[i+1]!=str1[i]:
            cnt2=1
            print(f'chara={str1[i+1]} and cnt={cnt2}')
            str2=str2+str1[i+1]
            str2=str2+str(cnt2)
    if str1[i]==str1[len(str1)-1]:
        cnt2+=1
print(str2)