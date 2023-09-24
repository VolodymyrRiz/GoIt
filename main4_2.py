args = ''
item = [*args]
recept = ''


def format_ingredients(*item):
    
    recept = ''
    print(item)
    i = 0
    i_len = len(*item)
    print(i_len)
    # if i_len == 1:
    #     for komp in item:
    #         recept = komp
    #         print(recept)
    #         return recept
                
            
    for komp in item:
        i = i + 1
        if i_len == 1:
            print(komp)
            recept = f'{komp}'
            return recept
        # if i_len == 2:
        #     print(komp)
        #     recept = f'{komp}'
        #     return recept
        if i == 1:
            recept = f'{komp}' + ', '
            print(recept)
            continue
        if i == i_len - 1:
            recept = recept + f'{komp}' + ' and '
            continue
        if i == i_len:
            recept = recept + f'{komp}'
            print(recept)
            return recept
        else:
            recept = recept + f'{komp}' + ', '
            print(recept)
        
         
print(format_ingredients(['2 eggs', "1 liter sugar"]))
