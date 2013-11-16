#!/usr/bin/env python3.3
# calculates the amount of currency you can buy with a given budget.
# author kahlb, ltc donations welcome :) LSRLVCerfwbAxBEyZJ4JtcZPdVwxc4zWs2
budget = float(input("Enter the amount of currency you want to sell: "))
price = float(input("Enter the price of the currency you want to earn: "))
fee = 0.2
income = float(budget/price-(budget/price*(fee/100)))
print('You will earn {} units of the chosen currency (when transaction fee is {} percent)'.format(income, fee))


