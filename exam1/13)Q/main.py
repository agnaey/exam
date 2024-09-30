import add,sub,mul,div,mod,no
while True:
    print('''
          1.add
          2.sub
          3.mul
          4.div
          5.mod
          6.exit
          
''')
    ch=int(input('enter your choise:'))
    if ch==1:
        a,b=no.num()
        add.add(a,b)
    elif ch==2:
        a,b=no.num()
        sub.sub(a,b)
    elif ch==3:
        a,b=no.num()
        mul.mul(a,b)
    elif ch==4:
        a,b=no.num()
        div.div(a,b)
    elif ch==5:
        a,b=no.num()
        mod.mod(a,b)
    else:break
