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
        print("test =%s" % freq)
    except KeyError:
        pass
    prod_fre[prod]= freq
print("Product Frequency =%s" % prod_fre)

