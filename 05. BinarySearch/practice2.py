# 떡볶이 떡 만들기 201p

# 내 코드
n, m=map(int, input().split())
array=list(map(int, input().split()))
height=max(array)-1
array=[x-max(array)+1 for x in array]
while sum([x for x in array if x>0])<m:
    array=[x+1 for x in array]
    height-=1

print(height)

# 답안 참고 (Parametric Search)
n, m=map(int, input().split())
array=list(map(int, input().split()))
start=0
end=max(array)

result=0
while start<=end:
    mid=(start+end)//2
    if sum([x-mid for x in array if (x-mid)>0])<m:
        end=mid-1
    else:
        result=mid
        start=mid+1

print(result)