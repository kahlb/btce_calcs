#!/usr/bin/env python3.3
# this software calculates a targeted profit
# author toffifee, ltc donations welcome =) LSRLVCerfwbAxBEyZJ4JtcZPdVwxc4zWs2
amount = float(input('Enter the amount of currency you want to trade with: '))
goal = float(input("Enter the amount of currency you want to earn: "))
price_sell = float(input("Enter the current price of the currency you want to increase: "))
fee = float(0.2)
sell_earning = float(amount*price_sell-(amount*price_sell/100*0.2))
price_rebuy = float((sell_earning/(amount+goal))/100.02*100)
print('To earn the aimed amount you will have to rebuy at {} (when transaction fee is {} percent)'.format(price_rebuy, fee))
