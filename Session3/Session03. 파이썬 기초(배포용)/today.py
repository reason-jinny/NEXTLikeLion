a = "I like"
b = "python"
print(a+ " " + b)

money = 4920

if money > 5000:
    print("택시")
elif money > 1250:
    print("bus")
else:
    print("걸어")


for i in range(5):
    print("%d번째 반복 중" % i)
    print("하이" * i)


print("정수 출력 %d" % 123.12)

print("문자 출력 %c")


def add(a,b):
    return a + b

print("1과 2를 더하면 결과는 %d입니다.", add(10,1110))