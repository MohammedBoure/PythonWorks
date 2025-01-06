import arabic_reshaper
import DataBase

def arabic(text:str):
    return arabic_reshaper.reshape(text)


"""
1 | 30/30 3m | aze | aze | aze | qsd | aze
2 | 30/30 3m | qsd | qsd | aze | zaeaze | qsd
to :
[['1', '30/30 3m', 'aze', 'aze', 'aze', 'qsd', 'aze'], ['2', '30/30 3m', 'qsd', 'qsd', 'aze', 'zaeaze', 'qsd']]
"""
def convert_string_to_list(input_string):
    lines = input_string.strip().split('\n')
    result = [list(map(str.strip, line.split('|'))) for line in lines]
    return result

def serch_in_list(l1,l2): # need testing
    l1_length = len(l1)
    l1 = l1[1:]
    result = False 
    for i in l2:
        if len(i) != l1_length:
            continue
        x = 0
        a = True
        for _ in l1:
            x += 1
            a = a and _ == i[x]
        if a:
            return True
    return False


def relaod_of_data_metal():
    client = DataBase.DataHandling("clients.db")
    metal = DataBase.DataHandling("metal.db")

    client_list = client.fetch_all_data("Clients")
    metal_list = metal.fetch_all_data("Metal")
    for i in metal_list:
        s = 0
        for _ in client_list:
            try:
                if i[1] == _[1] and _[6] == "no":
                    s += int(_[4])
            except:s = 0
        metal.edit_data_row("Metal",int(i[0]),"Number_used",str(s))
    
