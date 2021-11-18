
# 1.Arithmetic operations
def func(n,m):
    if n==2 and m==3:
        print("add : ",n+m)
    elif n==4 and n==5:
        print("sub :",n-m)
    elif n==6 and n==2:
        print("mul:",n*m)
    else:
        print("div:",n/m)
func(2,3)

# 2.Binary sort
def bin_search(arr,val,start,end):
    if start == end:
        if arr[start]>val:
            return start
        else:
            return start+1
    if start>end:
        return start
    mid = int((start+end)/2)
    if arr[mid]< val:
        return bin_search(arr,val,mid+1,end)
    elif arr[mid]>val:
        return bin_search(arr,val,start,mid-1)
    else:
        return mid
def ins_sort(arr):
    for i in range(1,len(arr)):
        val = arr[i]
        j = bin_search(arr,val,0,i-1)
        arr = arr[:j]+[val]+arr[j:i]+arr[i+1:]
    print("The sorted array is:",arr)
ins_sort([1,38,90,13,0,17,12,72,31,52,100,8,54])


# 3. lambda function
def table(n):
    return lambda x:x*n
b = table(2)
for i in range(1,11):
    print(2,"*",i,"=",b(i))


# 4.factors
num = int(input("Enter a number:"))
factors =[]
for i in range(1,num+1):
    if num%i==0:
        factors.append(i)
print("factors of {} = {}".format(num,factors))


# 5.Square root
import math
x = int(input("Enter a number:"))
print(math.sqrt(x))


# 6.Prime number
a = int(input("Enter the number:"))
c = 0
for i in range(2,int(a/2)+1):
    if (a%i)==0:
        c =1
        break
if c==0:
    print("It is a prime number")
else:
    print("It is not a prime number")

