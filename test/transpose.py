matrix = [
[1, 2, 3, 4],

[4, 5, 6, 7],

[7, 8, 9, 0]]

transposed = []

for i in range(4):

    print("we are going to take the ",i,"th element of each row")

    lst = []

    for row in matrix:

        print("the row we are considering :", row, "and we are going to add", row[i],"to a temporary list")

        lst.append(row[i])

    print("the ",i,"th column elements = ", i ,"th elements in every row are =", lst)

    transposed.append(lst)

    print("="*90)

print(transposed)