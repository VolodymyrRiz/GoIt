# borh = None
# sum = None
# #i = -1
# payment = ['10', '20', '30']
# borh_list = ['1', '-3', '4']
# #result = 0


# def amount_payment(payment, borh_list):
  
#     for sum in payment[:] and borh in borh_list[:]:
#         #global i
#         #global result
#         sum = int(sum)
#         borh = int(borh)
        
#         #i = i + 1
      
#         sum = sum + borh
#         #payment.insert(i, str(sum))
#         #result = result + sum
#         print(sum)
#     #print(result)
#     #return payment
   

# #amount_payment(['10', '20', '30', "1", "-3", "4"])

# amount_payment(payment, borh_list)

borh = 0
sum = None
#i = -1
payment = ['a', 'b', 'c', 'd', 'e', 'f']
#borh_list = ['d', 'e', 'f']
#result = 0


def amount_payment(payment):
  
    for sum in payment[0:5]:
        #global i
        #global result
        
        sum = int(sum)
        borh = int(borh)
        
        #i = i + 1
      
        sum = sum + borh
        #payment.insert(i, str(sum))
        #result = result + sum
        print(sum)
    #print(result)
    #return payment
   

amount_payment(['10', '20', '30', "1", "-3", "4"])