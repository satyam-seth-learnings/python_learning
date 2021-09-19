# list inside list
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1])
for i in matrix:
    print(i)
for i in matrix:
    for j in i:
        print(j)
print(matrix[2][0])