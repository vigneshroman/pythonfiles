from math import*
intArray = [int(i) for i in input().split()]
gcdAndIndex =[]
for i in range(0,len(intArray)):
  for j in range(i+1,len(intArray)):
    print(intArray[i],intArray[j])
    gcdval = gcd(intArray[i],intArray[j])
    indx = j-i
    gcdAndIndex.append((gcdval,indx))
#maximum = sum(list(max(gcdAndIndex)))
maximum = sum(max(gcdAndIndex))
