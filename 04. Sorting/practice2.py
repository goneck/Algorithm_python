# 성적이 낮은 순서로 학생 출력하기 180p

n=int(input())
array=[]
for i in range(n):
    input_data=input().split()
    array.append((input_data[0], int(input_data[1])))

# def setting(data):
#     return data[1]


# lambda 매개변수 : 표현식
array.sort(key=lambda student: student[1])
for student in array:
    print(student[0],end=' ')
