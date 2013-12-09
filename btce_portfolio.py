#!/usr/bin/env python2.7
# this software calculates the current value of your portfolio
# author kahlb, ltc donations welcome :) LSRLVCerfwbAxBEyZJ4JtcZPdVwxc4zWs2
fee=0.2
feecalc=1-(fee/100)     #makes the fee easier to calc. Just multiply with this value.
currnumber = input("Enter the number of different currencies in your portfolio: ")
# This contains the list of the currencies which will be calculated:
currlist = []
# This contains the prices to the currencies. It's always a pair, so pricelist[1] belongs to currlist[1]:
pricelist = []
# This reads the amount of currencies, for as many currencies as given in currnumber:
for n in range(currnumber):
	currlist.append(input("Enter the amout of currency {} in your portfolio: ".format(n+1)))
# Does the same as above, but reads the prices.
for n in range(currnumber):
	pricelist.append(input("Enter the price of currency {} to Bitcoin: ".format(n+1)))
btcprice = input("Enter the current Bitcoin Price: ") # Reads price for bitcoin. No currency specified by intention.
portfolio = 0
# This calculates the value of the portfolio in bitcoin, considering the fees for every necessary transaction.
for n in range(currnumber):
	portfolio = portfolio+(currlist[n]*pricelist[n]*feecalc)
capital = portfolio*btcprice*feecalc # This converts the bitcoins into another currency (USD, EUR, RUR or whatever you like)
print(portfolio)
print('Your portfolio is worth {} (when transaction fee is {} percent)'.format(capital, fee))


