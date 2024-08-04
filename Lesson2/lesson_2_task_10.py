def bank(money, year):
    for i in range(year):
        money = money + money * 0.5
    return money
print(bank(10000, 5))