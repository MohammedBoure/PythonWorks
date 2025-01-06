import pyautogui
from sockelab import MultiplayerServer
from time import sleep

global server
server = MultiplayerServer("127.0.0.1")

def addvec3(v1,v2):
    return (v1[0]+v2[0],v1[1]+v2[1],v1[2]+v2[2])

def divvec3(v,num:int):
    return (v[0]//num,v[1]//num,v[2]//num)

def filter(x,y,pixels):
    p1 = pixels[x,y]
    p2 = pixels[x+1,y]
    p3 = pixels[x,y+1]
    p4 = pixels[x+1,y+1]
    return divvec3(addvec3(addvec3(addvec3(p1,p2),p3),p4),4)


def talle3bit(x):
    if len(x)==3:
        return x
    elif len(x)==2:
        return "0"+x
    elif len(x)==1:
        return "00"+x
    else:return "000"
        
def filter2(x,y,r,g,b):
    return talle3bit(x)+talle3bit(y)+talle3bit(r)+talle3bit(g)+talle3bit(b)

def screnshot_pixel():
    screenshot = pyautogui.screenshot()
    width, height = screenshot.size
    pixel_data = screenshot.load()
    #list_data_image = []
    
    for y in range(0,height,2):
        for x in range(0,width,2):
            #list_data_image.append(((x//2,y//2),filter(x,y,pixel_data)))
            rgb = filter(x,y,pixel_data)
            sssss= filter2(str(x//2),str(y//2),str(rgb[0]),str(rgb[1]),str(rgb[2]))
            server.cycle_send(sssss)
    #server.cycle_send("000000000000000")
    #return list_data_image

while True:
    sleep(2)
    screnshot_pixel()
    print(1)
