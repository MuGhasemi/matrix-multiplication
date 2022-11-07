mat1 = []
mat2 = []
n = int(input("n row :"))
m = int(input("m column :"))
l = int(input("l column :"))
print("------------------MATRIX 1--------------------")
for i in range(n):
    listValue1 = [] 
    for j in range(m):
        value1 = int(input(f"matrix[{i}][{j}] :"))
        listValue1.append(value1)
    mat1.append(listValue1)
for i in range(n):
    for j in range(m):
        print(mat1[i][j],end=" ")
    print()
print("------------------MATRIX 2--------------------")
for k in range(m):
    listValue2= []
    for w in range(l):
        value2 = int(input(f"matrix[{k}][{w}] :"))
        listValue2.append(value2)
    mat2.append(listValue2)
for i in range(m):
    for j in range(l):
        print(mat2[i][j],end=" ")
    print()
print("------------------RESULT--------------------")
result = [[0 for i in range(l)] for j in range(n)]
for x in range(n):
    for y in range(l):
        for z in range(m):
            print(f"{result[x][y]}+{mat1[x][z]}*{mat2[z][y]}=",result[x][y]+mat1[x][z]*mat2[z][y],end="|")
            result[x][y]+=mat1[x][z]*mat2[z][y] #result[x][y] = result[x][y]+mat1[x][z]*mat2[z][y]
        print()
for i in range(n):
    for j in range(l):
        print(result[i][j],end=" ")
    print()
