x = int(input())
y = int(input())
z = int(input())
n = int(input())
lst = [0,0,0]
fnl_lst = []
for i in range (x+1):
    for j in range(y+1):
        for k in range(z+1):
            lst = [i,j,k]
            if sum(lst) == n:
                abdullah = 1
            else:
                fnl_lst.append([i,j,k])
print(fnl_lst)
