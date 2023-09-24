args = ''
item = [*args]
#recept = ''


def format_ingredients(item):


    if item == None:
        recept = None
        return recept
    
    recept = ''
    i = 0
    i_len = len(item)     
            
    for komp in item:
        i = i + 1
        
        if i_len == 1:
            recept = f'{komp}'
            return recept
        if i == 1 and i_len != 2:
             recept = f'{komp}' + ', '
             continue
        if i == 1 and i_len == 2:
            recept = f'{komp}' + ' and '
            continue
        if i == i_len - 1:
            recept = recept + f'{komp}' + ' and '
            continue
        if i == i_len:
            recept = recept + f'{komp}'
            return recept
        else:
            recept = recept + f'{komp}' + ', '
                
         
print(format_ingredients(["www", 'eee']))
