
def point_in_rect(rect:tuple, point:tuple):
    x, y, dx, dy = rect
    xp, yp = point
    if x < xp < x + dx and y < yp < y + dy:
        return True
    else:
        return False
    

def remove_data_repit_in_list(data_list):  # [[(a,b,c,d),x]]
    for item in data_list:
        for other_item in data_list:
            if item[0] == other_item[0] and item != other_item:
                item[1] += other_item[1]
                data_list.remove(other_item)
    return data_list     


def finition(list1,list2):
    for i in list1:
        for j in list2:
            if i[0]==j[0]:
                if i[1] > j[1]:
                    list1[list1.index(i)][1] = i[1]-j[1]
                    list2.pop(list2.index(j)) 
                elif i[1] < j[1]:
                    list2[list2.index(j)][1] = j[1]-i[1]
                    list1.pop(list1.index(i))
                elif i[1] == j[1]:
                    list1.pop(list1.index(i))
                    list2.pop(list2.index(j))
                    
def point_to_place_rect(point,Measurement):
    return ((point[0]//(800//Measurement))*80,(point[1]//(600//Measurement))*60,(800//Measurement),(600//Measurement))



def Number_of_bounding_squares(listp1,cplistp1,cplistp2,Increasing):
    for _ in listp1:
        cpt = 0
        x,y,dx,dy = _[0]
        x,y = x-dx,y
        if (x,y,dx,dy) in cplistp1:
            cpt += Increasing
        if (x,y,dx,dy) in cplistp2:
            cpt -= Increasing
        x,y,dx,dy = _[0]
        x,y = x+dx,y
        if (x,y,dx,dy) in cplistp1:
            cpt += Increasing
        if (x,y,dx,dy) in cplistp2:
            cpt -= Increasing
        x,y,dx,dy = _[0]
        x,y = x,y+dy
        if (x,y,dx,dy) in cplistp1:
            cpt += Increasing
        if (x,y,dx,dy) in cplistp2:
            cpt -= Increasing
        x,y,dx,dy = _[0]
        x,y = x,y-dy
        if (x,y,dx,dy) in cplistp1:
            cpt += Increasing
        if (x,y,dx,dy) in cplistp2:
            cpt -= Increasing  
        
        listp1[listp1.index(_)][2] = cpt
        
        