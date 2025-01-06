import pygame
from function import point_in_rect, remove_data_repit_in_list, finition,Number_of_bounding_squares
from constants import BLACK, RED, BLUE, SCREEN_HEIGHT, SCREEN_WIDTH,FPS,MEASUREMENT
from server import MultiplayerServer,MultiplayerClient

class Game:
    def __init__(self, screen):
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.measurement = MEASUREMENT
        self.screen = screen
        
        self.font = pygame.font.Font(None, 40)
        self.data_net_list = []
        self.data_net_p1, self.data_net_p2 = [], []
        self.cp_data_net_p1, self.cp_data_net_p2 = [], []
        self.time_wait_for_check = 0
        self.timer = 0
        self.active_button1 = False
        self.active_button2 = False
        self.pos_click1 = self.out_of_bounds()
        self.pos_click2 = self.out_of_bounds()
        self.recv_data_net_num = 0
        self.wait_time = 0  
        self.timer = 0  
        self.increasing = 1
        self.Waiting_time_before_moving = 0
        
        self.multiplayer = False
        self.mode_network = 1
        if self.multiplayer:
            if self.mode_network == 1:
                self.connect = MultiplayerServer('192.168.43.164')
            elif self.mode_network == 2:
                self.connect = MultiplayerClient('192.168.43.164')

    def out_of_bounds(self):
        return (self.SCREEN_WIDTH + 100, self.SCREEN_HEIGHT + 100)

    def draw_grid(self):
        for _ in range(self.measurement):
            pygame.draw.line(self.screen, BLACK, (0, _ * (self.SCREEN_HEIGHT // self.measurement)), 
                             (self.SCREEN_WIDTH, _ * (self.SCREEN_HEIGHT // self.measurement)), 5)
            pygame.draw.line(self.screen, BLACK, (_ * (self.SCREEN_WIDTH // self.measurement), 0), 
                             (_ * (self.SCREEN_WIDTH // self.measurement), self.SCREEN_HEIGHT), 5)

    def add_net_data(self):
        for i in range(self.measurement):
            for j in range(self.measurement):
                self.data_net_list.append(
                    (i * (self.SCREEN_WIDTH // self.measurement), 
                     j * (self.SCREEN_HEIGHT // self.measurement),
                     self.SCREEN_WIDTH // self.measurement,
                     self.SCREEN_HEIGHT // self.measurement)
                )

    def add_players(self):
        p1_pos = (self.SCREEN_WIDTH - (self.SCREEN_WIDTH // self.measurement), 
                  self.SCREEN_HEIGHT - (self.SCREEN_HEIGHT // self.measurement))
        p2_pos = (0, 0)
        p_size = (self.SCREEN_WIDTH // self.measurement, self.SCREEN_HEIGHT // self.measurement)
        
        self.data_net_p1.append([(*p1_pos, *p_size), 0,0])
        self.cp_data_net_p1.append((*p1_pos, *p_size))
        self.data_net_p2.append([(*p2_pos, *p_size), 0,0])
        self.cp_data_net_p2.append((*p2_pos, *p_size))

    def first_creation(self):
        if self.multiplayer:
            if self.mode_network == 1:
                data_net = f"{self.measurement}_{self.SCREEN_HEIGHT}_{self.SCREEN_WIDTH}E"
                self.connect.cycle_send(data_net)
            elif self.mode_network == 2:
                data = self.connect.cycle_recv()
                if data[-1] == "E":
                    data = data[:-1]
                    self.measurement, self.SCREEN_HEIGHT, self.SCREEN_WIDTH = data.split("_")
                    self.measurement, self.SCREEN_HEIGHT, self.SCREEN_WIDTH = int(self.measurement), int(self.SCREEN_HEIGHT), int(self.SCREEN_WIDTH)

        self.draw_grid()
        self.add_net_data()
        self.add_players()
        self.paint()

    def create_text_in_screen(self, data_net: int, place: tuple):
        text = self.font.render(str(data_net), True, (0, 0, 0))
        self.screen.blit(text, place)

    def paint(self):
        for rect in self.data_net_p1:
            pygame.draw.rect(self.screen, RED, rect[0])
        for rect in self.data_net_p2:
            pygame.draw.rect(self.screen, BLUE, rect[0])
    def handle_clicks(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.active_button1:
                self.pos_click1 = event.pos
                self.time_to_distance(self.first_click,self.pos_click1)
                self.active_button1 = False
                
                if self.multiplayer and self.mode_network == 1:
                    try:
                        self.connect.cycle_send(self.send_game_data(event.pos,self.num_of_rect1,self.first_click))
                    except:pass
                    
                    
            elif self.active_button2:
                self.pos_click2 = event.pos
                if not self.first_click:
                    self.first_click = 0
                self.time_to_distance(self.first_click,self.pos_click2)
                self.active_button2 = False
                
                if self.multiplayer and self.mode_network == 2:
                    try:
                        self.connect.cycle_send(self.send_game_data(event.pos,self.num_of_rect2,self.first_click))
                    except:pass
            

    def handle_right_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and not self.active_button1 and not self.active_button2:
            if self.mode_network == 1 and self.multiplayer:
                for p1 in self.data_net_p1:
                    if point_in_rect(p1[0], event.pos):
                        self.active_button1 = True
                        self.num_of_rect1 = p1[1]
                        self.first_click = event.pos
                        p1[1] = 0
                        break
            elif self.mode_network == 2 and self.multiplayer:
                for p2 in self.data_net_p2:
                    if point_in_rect(p2[0], event.pos):
                        self.active_button2 = True
                        self.num_of_rect2 = p2[1]
                        self.first_click = event.pos
                        p2[1] = 0
                        break
            else:
                for p1 in self.data_net_p1:
                    if point_in_rect(p1[0], event.pos):
                        self.active_button1 = True
                        self.num_of_rect1 = p1[1]
                        self.first_click = event.pos
                        p1[1] = 0
                        break
                for p2 in self.data_net_p2:
                    if point_in_rect(p2[0], event.pos):
                        self.active_button2 = True
                        self.num_of_rect2 = p2[1]
                        self.first_click = event.pos
                        p2[1] = 0
                        break

    def event(self, event):
        self.handle_clicks(event)
        self.handle_right_click(event)
    
    def recv_data(self,data_net):
        self.recv_data_net_num = data_net 
        
    def send_game_data(self, pos_click, num_of_rect,first_click):
        x, y = pos_click
        xf,yf = first_click
        x, y, num ,xf , yf = str(x), str(y), str(num_of_rect) , str(xf) , str(yf)
        return f"{xf}_{yf}_{x}_{y}_{num}"
    
    def recv_game_data(self, data):
        try:
            x, y, num, xf, yf = map(int, data.split("_"))
            if self.mode_network == 2:
                self.pos_click2 = (x, y)
                self.num_of_rect2 = num
                self.first_click = (xf, yf)
            elif self.mode_network == 1:
                self.pos_click1 = (x, y)
                self.num_of_rect1 = num
                self.first_click = (xf, yf)
        except ValueError:
            print("Error: Received malformed data", data)


    def cicle(self):
        if self.multiplayer and self.mode_network == 2:
            data = self.connect.cycle_recv()
            print(data)
            if data:
                print("Received data:", data)
                self.recv_game_data(data)   
        
        elif self.multiplayer and self.mode_network == 1:
            data = self.connect.cycle_recv()
            self.recv_game_data(data)
        
        self.timer += 1  
        if self.recv_data_net_num%10 == 0:
            self.paint()
        
        if self.pos_click1 != self.out_of_bounds():
            if self.timer >= self.wait_time * FPS:  
                self.update_positions(self.pos_click1, self.num_of_rect1, self.data_net_p1, self.cp_data_net_p1,self.cp_data_net_p2)
                self.pos_click1 = self.out_of_bounds()

        if self.pos_click2 != self.out_of_bounds():
            if self.timer >= self.wait_time * FPS:  
                self.update_positions(self.pos_click2, self.num_of_rect2, self.data_net_p2, self.cp_data_net_p2,self.cp_data_net_p1)
                self.pos_click2 = self.out_of_bounds()

        if self.timer % FPS == 0:
            self.paint()
            for p1 in self.data_net_p1:
                self.create_text_in_screen(p1[1], (p1[0][0], p1[0][1]))
                p1[1] += 1 + p1[2]
                if p1[1] <= 0:p1[1]=0
                    
            for p2 in self.data_net_p2:
                self.create_text_in_screen(p2[1], (p2[0][0], p2[0][1]))
                p2[1] += 1 + p2[2]
                if p2[1] <= 0:p2[1]=0
                    
            self.recv_data_net_num = 0

    def time_to_distance(self,pos1,pos2):
        self.distance = ((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)**(1/2)
        print(self.distance)

    def update_positions(self, pos, rect_num, data_net_p, cp_data_net,cp_data_net2):
        
        self.timer = 0
        for rect in self.data_net_list:
            if point_in_rect(rect, pos) and rect_num > self.time_wait_for_check:
                data_net_p.append([rect, rect_num,0])
                cp_data_net.append(rect)
                data_net_p = remove_data_repit_in_list(data_net_p)
                list(set(cp_data_net))
                finition(self.data_net_p1, self.data_net_p2)
        Number_of_bounding_squares(data_net_p,cp_data_net,cp_data_net2,self.increasing)
        try:
            self.wait_time = self.distance*self.Waiting_time_before_moving
        except:self.wait_time = 0
