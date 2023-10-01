#password = 'NmlDl1V0'
#password = 'z,qrE*IE'
password = ''
false1 = False
true1 = True
flag = 0

def search_method(char):
    
    global flag

    #password = 'absdfrnt'
    if char in password:
        flag = 1
        true1 = True
        return true1
    else:
        false1 = False
        return false1


def is_valid_password(password):
    big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small = 'abcdefghijklmnopqrstuvwxyz'
    global flag
    number = '012345678'
    
    if len(password) == 8:
        #print(len(password))
        for char in big:
            print(flag)
            search_method(char)
        if flag == 0:
            return False
        if false1 == False and flag == 1 and true1 == True:
            flag = 0
            for char in small:
                search_method(char)
            if flag == 0:
                return False
            if false1 == False and flag == 1 and true1 == True:
                flag = 0
                for char in number:
                    
                    search_method(char)
                if flag == 0:
                    return False
                if false1 == False and flag == 1 and true1 == True:
                    return True
                
          
    else:
        return False
            
     
print(is_valid_password('NmlDl1V0'))    