points = {(0, 1): 2, (0, 2): 3.8, (0, 3): 2.7, (1, 2): 2.5, (1, 3): 4.1, (2, 3): 3.9}

def calculate_distance(coordinates):
    
    #points = {(0, 1): 2, (0, 2): 3.8, (0, 3): 2.7, (1, 2): 2.5, (1, 3): 4.1, (2, 3): 3.9}
    
    res = 0
    count = 0
    len_coor = len(coordinates)
    
    if coordinates == ['']:
        return [0]

    for key in coordinates:
        
        if count < len_coor - 1:
                        
            char = coordinates[count:count+2]
            
            char_1 = char[0]
            char_2 = char[1]
            if char_1 > char_2:
                char.reverse()
                
            count += 1
            char = tuple(char)
            if char in points:
                res_1 = points.get(char)
                
                res = res + res_1
                          
            else:
                continue
 
    return res

        
print(calculate_distance([0, 1, 3, 2, 0, 2]))