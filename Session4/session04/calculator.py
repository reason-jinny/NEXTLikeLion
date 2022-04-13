class Calculator:
    def __init__(self,name):
        self.name = name
        self.age = age
        self.result = 0
    
    def add(self,num):
        self.result += num
        return self.result
    
    def sub(self,num):
        self.result -= num
        return self.result

    def mul(self,num):
        self.result *= num
        return self.result

    def div(self,num):
        self.result /= num
        return self.result


calculator1 = Calculator("이유진")

print(calculator1.result)
