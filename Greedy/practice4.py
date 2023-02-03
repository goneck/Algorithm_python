# 1이 될 때까지 99p

# 첫번째 방법
# n, k=map(int, input().split())

# count=0
# while True:
#     if n==1:
#       break
#     if n%k==0:
#         n=n//k
#     else:
#         n-=1
#     count+=1

# print(count)

# 두 번째 방법
n, k=map(int, input().split())
count=0

while n>=k:
    if n%k==0:
        n=n//k
        count+=1
    else:
        count+=n%k
        n-=n%k


count+=(n-1)

print(count)
