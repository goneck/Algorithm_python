# 다이나믹 프로그래밍 실버5

# 아니 다리 겹치면 안된다면서 (교차되면 안된다는 의미로 받아들임)
# 조합으로 푸는 문제였다
import math


n=int(input())
for i in range(n):
    n, m=map(int, input().split())
    print(int(math.factorial(m)//(math.factorial(m-n)*math.factorial(n))))
        