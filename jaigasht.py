import random
n = int(input("please Enter N "));
L = set();
while len(L)< n+1:
    rand = random.randint(0,n);
    L.add(rand);
    #print(rand);
print(L);