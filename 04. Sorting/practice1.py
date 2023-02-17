# 위에서 아래로 178p

n=int(input())
li=[]
for i in range(n):
    li.append(int(input()))

li.sort(reverse=True)

for i in range(n):
    print(li[i], end=' ')
