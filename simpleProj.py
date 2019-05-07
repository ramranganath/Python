# This Program
# a. it wil pull out all the details from file
# b. list unique user id's
# c. how many products bought by each user.
# d. distinct product bought by each user
#e.  how many times each product bought in total.

f=open("D:/imp/Python/test/testdata.txt", 'r')
unique_users =set()
dist_prods =set()
x=f.readline()
while(x !=""):
    temp= x.strip().split(",")
    id, prod=temp[0], temp[2]
#    prod=temp[2]
    unique_users.add(id)
    dist_prods.add(prod)
    x= f.readline()

print("List of Unique Users %s" % unique_users)
print("Number of Unique users %d :" % len(unique_users))
print("List of Distinct Products %s" % dist_prods)

# byfurcate products bought by each customer
# to detect the Product purchase frequency
f=open("D:/imp/Python/test/testdata.txt", 'r')
user_prod ={}
x = f.readline()
while(x!=""):
    temp= x.strip().split(",")
    id, prod=temp[0], temp[2]
    set_products=set()
    try:
        set_products=user_prod[id]
    except KeyError:
        set_products=set()
    set_products.add(prod)
    user_prod[id]=set_products
    x= f.readline()

print("User Product Dictionary %s"  % user_prod)




# to detect the Product purchase frequency
f=open("D:/imp/Python/test/testdata.txt", 'r')
prod_fre ={}
lines = f.readlines()
for x in lines:
    temp= x.strip().split(",")
    prod = temp[2]
    freq = 1
    try:
        freq = prod_fre[prod] + 1
    except KeyError:
        pass
    prod_fre[prod]= freq
#    print("Product Frequency =%s" % prod_fre)
print("Product Frequency = %s" % prod_fre)

# to detect the Product purchase frequency
f=open("D:/imp/Python/test/testdata.txt", 'r')
prod_fre ={}
lines = f.readlines()
for x in lines:
    temp= x.strip().split(",")
    prod = temp[2]
    freq = 1
    try:
        freq = prod_fre[prod] + 1
 #       print("test =%s" % freq)
    except KeyError:
        pass
    prod_fre[prod]= freq
print("Product Frequency = %s" % prod_fre)