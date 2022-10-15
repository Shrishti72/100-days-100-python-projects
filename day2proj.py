print('welcome to the tip calulator')
bill=float(input("what was the total bill?"))
print('${}'.format(bill))
a,b,c=10,12,15
Tip=int(input('''What percantage tip would you like to give?\n 10%\n12%\n15%\n'''))
toltip=bill*(Tip/100)
e=bill+toltip
ppl=int(input('How many people to split the bill?'))
d=e/ppl
final=round(d,2)
print("Each person should pay: ${}".format(final))

