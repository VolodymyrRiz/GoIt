borh = 0
sum = None
i = -1
payment = list()
dani = list()
result = 0


def amount_payment(payment):
  
    for sum in payment[:]:
        global i
        global result
        sum = int(sum)
        i = i + 1
      
        sum = sum + borh
        #payment.insert(i, str(sum))
        result = result + sum
        print(sum)
    print(result)
    #return payment
   

amount_payment('10', '20', '30')
pass