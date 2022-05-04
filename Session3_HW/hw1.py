# 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보세요. 

#(단 입력으로 들어오는 수의 개수는 정해져 있지 않으며,
# 입력값으로 -1이 들어오면 더 이상 값을 받지 않는다.)

list = []
answer = 0

while True :
    num = int(input("당신이 입력하는 수의 평균을 계산해 줄게요:"))
    if num == -1 :
        break
    list.append(num)
    answer = sum(list)/len(list)
    
print(answer)