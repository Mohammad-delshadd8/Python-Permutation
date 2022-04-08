import random
n = int(input("please Enter N "));
L = list();
while len(L)< n+1:
    rand = random.randint(0,n);
    if rand not in L:
     L.append(rand);
    #print(rand);
print(L);
