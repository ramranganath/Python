# listing the prime numbers between Range from 2 to till ...

for i in range(2,60):
    j=2
    counter=0
    while(j<i):
        if i%j==0:
            counter=1
            j=j+1
        else:
            j=j+1
            
    if counter==0:
        print(str(i) +" is a Prime Number")
    else:
        counter=0
        
"""        
for a in range(0,45,2):
    print(str(a) +" Even")

for o in range(1,45,2):
    print(str(o) +" Odd Nums")

day = "Monday"

if day=="Tuesday" or day == "Monday":
    print("Today is Sunny")
else:
    print("Today is Rainy")
    
wt =60

for i in range(0,10):
    mwgt = wt/6
    print(mwgt)
    wt=wt+1
"""
    
    