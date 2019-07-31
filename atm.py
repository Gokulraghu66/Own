bal=1000
ch=3
pin=1234
while ch>=0:
  print('Enter ur pin')
  pi=int(input())
  if(pi==pin):
    print('Press 1 for Balance\n')
    print('Press 2 To Make a Withdrawl\n')
    print('Press 3 To Deposit\n')
    op=int(input('Enter ur option '))
    if(op==1):
      print(bal)
      break
    elif(op==2):
      print('Enter ur amount')
      amount=int(input())
      if(amount<=bal):
        print(bal-amount)
        break
      else:
        print('Enter valid amount.Ur balance is',bal)
    elif(op==3):
      print('Enter ur amount to add')
      amount=int(input())
      print(amount+bal)
      break
  elif pin != ('1234'):        
    ch=ch-1
    if ch==0:
      print('Sorry ur not right person')
      break
