class Fishbread:
    def __init__(self,flavor,price,amount):
        self.flavor = flavor
        self.price = price
        self.amount = amount

    def one_more(self):
        self.price += 1000
        self.amount += 1

fishbread1 = Fishbread("팥",1000,1)
fishbread2 = Fishbread("슈크림",1200,1)
fishbread3 = Fishbread("팥",1500,1)

fishbread1.one_more()
fishbread1.one_more()

print(fishbread1.amount)