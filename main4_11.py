


def is_valid_password(password):
    
    big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small = 'abcdefghijklmnopqrstuvwxyz'
    flag = 0
    number = '012345678'
    
    if len(password) == 8:
        pass
    else:
        return False

    for char in big:
        print(char)
        if char in password:
            flag = flag + 1
            print(flag)
    if flag == 0:
        return False
    else:
        flag = 0
        for char in small:
            print(char)
            if char in password:
                flag = flag + 1
                print(flag)
        if flag == 0:
            return False
        else:
            flag = 0
            for char in number:
                print(char)
                if char in password:
                    flag = flag + 1
                    print(flag)
            if flag == 0:
                return False
            else:
                
                return True