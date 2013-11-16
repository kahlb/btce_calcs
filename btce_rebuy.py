#!/usr/bin/env python3.3
# calculates the profit from a certain sell/rebuy situation
# author kahlb, ltc donations welcome :) LSRLVCerfwbAxBEyZJ4JtcZPdVwxc4zWs2
amount_sell = float(input('Enter the amount of currency you want to trade with: '))
price_sell = float(input('Enter the current price of the currency you want to rebuy: '))
fee = float(0.2)
earning = float(price_sell*amount_sell-(price_sell*amount_sell/100*fee))
print ('You will earn {} from this trade'.format(earning))
price_rebuy = float(input('Enter the price to which you plan to rebuy: '))
amount_rebuy = float(earning/price_rebuy-(earning/price_rebuy/100*fee))
increase = amount_rebuy - amount_sell
print('You will increase your currency by {} with this trade when you rebuy {} units of the currency to the given price (when transaction fee is {} percent)'.format(increase, amount_rebuy, fee))
