#!/usr/bin/env python2.7
# this software calculates the current value of your portfolio
# author kahlb, ltc donations welcome :) LSRLVCerfwbAxBEyZJ4JtcZPdVwxc4zWs2
fee=0.2
feecalc=1-(fee/100)
currnumber = input("Enter the number of different currencies in your portfolio: ")
currlist = []
pricelist = []
for n in range(currnumber):
	currlist.append(input("Enter the amout of currency {} in your portfolio: ".format(n+1)))
for n in range(currnumber):
	pricelist.append(input("Enter the price of currency {} to Bitcoin: ".format(n+1)))
btcprice = input("Enter the current Bitcoin Price: ")
portfolio = 0
for n in range(currnumber):
	portfolio = portfolio+(currlist[n]*pricelist[n]*feecalc)
capital = portfolio*btcprice*feecalc
print(portfolio)
print('Your portfolio is worth {} (when transaction fee is {} percent)'.format(capital, fee))


