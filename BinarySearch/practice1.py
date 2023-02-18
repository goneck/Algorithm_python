# 부품 찾기 197p

# 이진 탐색 이용
n=int(input())
array=list(map(int, input().split()))
array.sort()

m=int(input())
check=list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start>end:
        return "n"
    mid=(start+end)//2
    if array[mid]==target:
        return "y"
    elif array[mid]>target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)



for item in check:
    if binary_search(array, item, 0, n-1)=="n":
        print("no", end=' ')
    else:
        print("yes", end=' ')


# 계수 정렬 이용
n=int(input())
array=list(map(int, input().split()))
count_list=[0]*(max(array)+1)

for item in array:
    count_list[item]+=1

m=int(input())
check=list(map(int, input().split()))

for item in check:
    if count_list[item]!=0:
        print("yes", end=' ')
    else:
        print("no", end=' ')


# 집합 자료형 이용
n=int(input())
array=set(map(int, input().split()))

m=int(input())
check=list(map(int, input().split()))

for item in check:
    if item in array:
        print("yes", end=' ')
    else:
        print ("no", end=' ')
