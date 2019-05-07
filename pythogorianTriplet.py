#Pythogorian triplet
# a^2* b^2=C^2

nums=[5,4,7]
if(nums[0]**2== nums[1]**2+nums[2]**2 or nums[1]**2== nums[0]**2+nums[2]**2 or nums[2]**2== nums[1]**2+nums[0]**2):
    print("Pythogorian Triplet number")
else:
	print("Not a Pythogorian Triplet")
	

nums=[5,4,3]
h= max(nums)
nums.remove(h)
#squars =map(lambda x: x**2, nums)
squars = [i **2 for i in nums]
other_sqrs= sum(squars)
if(h**2 == other_sqrs):
    print("Pythogorian Triplet number")
else:
	print("Not a Pythogorian Triplet")

#Print all the Pythogorian triplets where hypo <=10

list_triplets = []
max_hyp=20
for i in range (1, max_hyp+1):
    for j in range(1, max_hyp+1):
	    for k in range(1, max_hyp+1):
	       if(i **2 + j **2 == k **2):
		       list_triplets.append((i, j, k))
print("Triplets between 1 to 10 are : %s" % list_triplets)

list_trips= [(i, j, k) for i in range (1, 11) for j in range(i+1, 11) for k in range(j+1,11) if(i **2 +j **2 == k **2)]
print("Simple way to type triplets %s" % list_trips)

