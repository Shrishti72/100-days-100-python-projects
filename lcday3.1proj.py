print("Welcome to Love Calculator")
her=input("enter her name")
his=input('enter his name')
nstr=her.lower() + his.lower()
t=nstr.count('t')
r=nstr.count('r')
u=nstr.count('u')
e=nstr.count('e')
true=t+r+u+e

l=nstr.count('l')
o=nstr.count('o')
v=nstr.count('v')
e=nstr.count('e')
love=l+o+v+e
perc=str(true)+str(love)
p=int(perc)
print('oohoo the love percentage is {}%'.format(p))
