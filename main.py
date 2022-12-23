
list=[]
n=int(input("enter no. of input"))
for i in range(n):
    b=int(input("enter"))
    list.append(b)
print(list)

prime=[]
composite=[]

length=len(list)
for j in range(length):
    for i in range(2,n):
         if (list[j]%i)==0:
            composite.append(list[j])
            break
    else:
     prime.append(list[j])
print(composite)
print(prime)





