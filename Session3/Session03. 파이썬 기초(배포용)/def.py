#함수를 '1개만' 작성해 
#공백으로 구분되어 입력받은 두 정수의 
#합, 차, 곱, 몫, 나머지를 한 줄씩 순서대로 출력하세요

x, y = map(int, input().split())

def hi(a,b):
    res = []
    res.append(a + b)
    res.append(a - b)
    res.append(a * b)
    res.append(a // b)
    res.append(a % b)
    return res

for i in hi(x,y):
    print(i)