#i) Write a script with two functions:

#1. is_prime - takes an integer argument and returns true or false
#2. find_primes - takes a list of integers and returns list of prime numbers in the input list
#and example code to call find_primes

def is_prime(num):
    cnt=0
    for i in range(1,num+1):
        if num%i==0:
            cnt+=1
    
    if cnt<=2:
        print("True")
    else:
        print("false")

num=int(input("Please give a numbre="))
is_prime(num)

def call_prime(plist):
    
    for num in plist:
        cnt=0
        for i in range(1,num+1):
            if num%i==0:
                cnt+=1
        if cnt<=2:
            print(f'{num} is a prime number')
        else:
            print(f'{num} is a composite number')
plist=[2,4,7,9,17,22]
call_prime(plist)