# comments here

ages = [10,20,30, 40]
incomes = [100,200,300, 400]

def calcAvg (list):
    sum = 0
    for i in list:
        sum = sum + i
    
    return sum/len(list)

print(calcAvg(incomes))