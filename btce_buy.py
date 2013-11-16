#!/usr/bin/env python3.3
# this software calculates a buy scenario
# author kahlb, ltc donations welcome :) LSRLVCerfwbAxBEyZJ4JtcZPdVwxc4zWs2
budget = input("Enter the amount of currency you want to spend: ")
price = input("Enter the price of the currency you want to buy: ")
fee = 0.2
buyable = budget*price*fee/100
print('You are able to buy {} units of the currency (when transaction fee is {} percent)'.format(buyable, fee))


