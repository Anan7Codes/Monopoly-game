import pygame,functions

pygame.init()

display_width = 1430
display_height = 800
card_length = 130
card_breadth = 60
boxl = 350
boxb = 215
gapv = (display_height - 2*boxl)/3
gaph = (display_width - display_height - 2*boxb)/3
cardl = 0.1*boxb
cardh = 0.1*boxl
cgaph = ((boxb/2)-(3*cardl))/4
cgapv = 0.05*boxl
c2gaph= ((boxb/2)-(2*cardl))/3
tflag = 0
timer = 8



white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
red = (255,50,0)
blue = (0,0,255)
green = (50,255,50)
back = (100,10,100)
new = (10,100,100)
new1 = (200,150,50)
new2 = (67,234,169)
orange = (228,142,88)
grey = (160,160,160)

clock = pygame.time.Clock()



class Property():

    def __init__(self,name,color,country,locx,locy,cost,x1,y1,x2,y2):
        self.name = name
        self.color = color
        self.country = country
        self.locx = locx
        self.locy = locy
        self.cost = cost
        self.rent = 0.1*self.cost
        self.house1 = 0.4*self.cost
        self.house2 = 0.5*self.cost
        self.house3 = 0.6*self.cost
        self.hotel = self.cost
        self.mortgage = 0.4*self.cost
        self.no_of_houses = 0
        self.owner = None
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    def locmaker(self):
        lfont = pygame.font.Font('freesansbold.ttf',10)
        if self.locx == card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[0,self.locy-card_breadth/2,card_length,card_breadth],1)
            functions.text_in_box(self.name,lfont,black,0,self.locy-card_breadth/2,0.7*card_length,card_breadth)
            functions.gameDisplay.fill(self.color, rect = [0.7*card_length,self.locy-card_breadth/2,0.3*card_length,card_breadth])
        elif self.locx == display_height -  card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[display_height -  card_length,self.locy-card_breadth/2,card_length,card_breadth],1)
            functions.text_in_box(self.name,lfont,black,display_height -  0.7*card_length,self.locy-card_breadth/2,0.7*card_length,card_breadth)
            functions.gameDisplay.fill(self.color, rect = [display_height -  card_length,self.locy-card_breadth/2,0.3*card_length,card_breadth])
        elif self.locy == card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[self.locx-card_breadth/2,0,card_breadth,card_length],1)
            a = self.name.split(' ')
            temp = 0
            for x in a:
                functions.text_in_box(x,lfont,black,self.locx-card_breadth/2,temp,card_breadth,0.35*card_length)
                temp += 0.35*card_length
            functions.gameDisplay.fill(self.color, rect = [self.locx-card_breadth/2,0.7*card_length,card_breadth,0.3*card_length])
        elif self.locy ==  display_height -  card_length/2:
            pygame.draw.rect(functions.gameDisplay,black,[self.locx-card_breadth/2,display_height -  card_length,card_breadth,card_length],1)
            functions.text_in_box(self.name,lfont,black,self.locx-card_breadth/2,display_height -  0.7*card_length,card_breadth,0.7*card_length)
            functions.gameDisplay.fill(self.color, rect = [self.locx-card_breadth/2,display_height -  card_length,card_breadth,0.3*card_length])
        pygame.display.update() 

    def card(self):
        functions.gameDisplay.fill(white, rect = [170,400,200,250])
        lfont = pygame.font.Font('freesansbold.ttf',25)
        functions.text_in_box(self.name,lfont,self.color,170,410,200,30)
        functions.message_to_screen("Cost: $ %d"%self.cost,black,180,460,20)
        functions.message_to_screen("Rent: $ %d"%self.rent,black,180,480,20)
        functions.message_to_screen("1st floor: $ %d"%self.house1,black,180,500,20)
        functions.message_to_screen("2nd floor: $ %d"%self.house2,black,180,520,20)
        functions.message_to_screen("3rd floor: $ %d"%self.house3,black,180,540,20)
        functions.message_to_screen("Hotel: $ %d"%self.hotel,black,180,560,20)
        functions.message_to_screen("Mortgage value: $ %d"%self.mortgage,black,190,600,20)
        pygame.display.update()

    def squares(self):
        global tflag ,timer
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.owner == 0:
            pygame.draw.rect(functions.gameDisplay, self.color, [self.x1,self.y1,cardl,cardh])
            if self.x1 < mouse[0] < self.x1+cardl and self.y1 < mouse[1] < self.y1 + cardh:
                if click[0]==1:
                    tflag = 1
            
        if self.owner == 1:
            pygame.draw.rect(functions.gameDisplay, self.color, [self.x2,self.y2,cardl,cardh])
            if self.x2 < mouse[0] < self.x2+cardl and self.y2 < mouse[1] < self.y2 + cardh:
                if click[0]==1:
                    tflag = 1
        if tflag == 1:
            timer -= 1
            self.card()
            if timer == 0:
                flag = 0
                timer = 8
                

_property = { "delhi":Property("Delhi",red,"India",card_length + card_breadth/2,card_length/2,80000,display_height + gaph + cgaph,gapv + 0.2*boxl + cgapv,display_height + gaph + cgaph,2*gapv + boxl + 0.2*boxl + cgapv )
            , "mumbai":Property("Mumbai",red,"India",card_length + 5*(card_breadth/2),card_length/2,60000,display_height + gaph + 2*cgaph + cardl,gapv + 0.2*boxl + cgapv,display_height + gaph + 2*cgaph + cardl,2*gapv + boxl + 0.2*boxl + cgapv )
            , "banglore":Property("Banglore",red,"India",card_length + 7*(card_breadth/2),card_length/2,40000,display_height + gaph + 3*cgaph + 2*cardl,gapv + 0.2*boxl + cgapv,display_height + gaph + 3*cgaph + 2*cardl,2*gapv + boxl + 0.2*boxl + cgapv )  
            , "newyork":Property("New York",yellow,"America",card_length + 11*(card_breadth/2),card_length/2,70000,display_height + gaph + boxb/2 + cgaph,gapv + 0.2*boxl + cgapv,display_height + gaph + boxb/2 + cgaph,2*gapv + boxl + 0.2*boxl + cgapv)
            , "washingtondc":Property("Washington D.C.",yellow,"America",card_length + 13*(card_breadth/2),card_length/2,40000,display_height + gaph + boxb/2 + 2*cgaph + cardl,gapv + 0.2*boxl + cgapv,display_height + gaph + boxb/2 + 2*cgaph + cardl,2*gapv + boxl + 0.2*boxl + cgapv)
            , "sanfrancisco":Property("San Francisco",yellow,"America",card_length + 17*(card_breadth/2),card_length/2,60000,display_height + gaph + boxb/2 + 3*cgaph + 2*cardl,gapv + 0.2*boxl + cgapv,display_height + gaph + boxb/2 + 3*cgaph + 2*cardl,2*gapv + boxl + 0.2*boxl + cgapv)
            , "london":Property("London",blue,"England",display_height -  card_length/2,card_length + 1*(card_breadth/2),80000 ,display_height + gaph + cgaph,gapv + 0.2*boxl + 2*cgapv + cardh,display_height + gaph +2*cgapv + cardh,2*gapv + boxl + 0.2*boxl + 2*cgapv + cardh )
            , "manchester":Property("Manchester",blue,"England",display_height -  card_length/2,card_length + 3*(card_breadth/2),30000,display_height + gaph + 2*cgaph + cardl,gapv + 0.2*boxl + 2*cgapv + cardh,display_height + gaph + 2*cgaph + cardl,2*gapv + boxl + 0.2*boxl + 2*cgapv + cardh )
            , "oxford":Property("Oxford",blue,"England",display_height -  card_length/2,card_length + 7*(card_breadth/2),40000,display_height + gaph + 3*cgaph + 2*cardl,gapv + 0.2*boxl + 2*cgapv + cardh,display_height + gaph + 3*cgaph + 2*cardl,2*gapv + boxl + 0.2*boxl + 2*cgapv + cardh)
            , "melbourne":Property("Melbourne",green,"Australia",card_length/2,card_length + 1*(card_breadth/2),40000,display_height + gaph + boxb/2 + cgaph,gapv + 0.2*boxl + 2*cgapv + cardh,display_height + gaph + boxb/2 + cgaph,2*gapv + boxl + 0.2*boxl + 2*cgapv + cardh)
            , "canberra":Property("Canberra",green,"Australia",card_length/2,card_length + 3*(card_breadth/2),50000,display_height + gaph + boxb/2 + 2*cgaph + cardl,gapv + 0.2*boxl + 2*cgapv + cardh,display_height + gaph + boxb/2 + 2*cgaph + cardl,2*gapv + boxl + 0.2*boxl + 2*cgapv + cardh)           
            , "sydney":Property("Sydney",green,"Australia",card_length/2,card_length + 7*(card_breadth/2),70000,display_height + gaph + boxb/2 + 3*cgaph + 2*cardl,gapv + 0.2*boxl + 2*cgapv + cardh,display_height + gaph + boxb/2 + 3*cgaph + 2*cardl,2*gapv + boxl + 0.2*boxl + 2*cgapv + cardh)
            , "tokyo":Property("Tokyo",back,"Japan",card_length/2,card_length + 11*(card_breadth/2),70000,display_height + gaph + cgaph,gapv + 0.2*boxl + 3*cgapv + 2*cardh,display_height + gaph +2*cgapv + cardh,2*gapv + boxl + 0.2*boxl + 3*cgapv + 2*cardh )
            , "osaka":Property("Osaka",back,"Japan",card_length/2,card_length + 13*(card_breadth/2),50000,display_height + gaph + 2*cgaph + cardl,gapv + 0.2*boxl +3*cgapv + 2*cardh,display_height + gaph + 2*cgaph + cardl,2*gapv + boxl + 0.2*boxl + 3*cgapv + 2*cardh )
            , "hiroshima":Property("Hiroshima",back,"Japan",card_length/2,card_length + 17*(card_breadth/2),30000,display_height + gaph + 3*cgaph + 2*cardl,gapv + 0.2*boxl + 3*cgapv + 2*cardh,display_height + gaph + 3*cgaph + 2*cardl,2*gapv + boxl + 0.2*boxl + 3*cgapv + 2*cardh)
            , "beijing":Property("Beijing",new,"China",card_length + 1*(card_breadth/2),display_height - card_length/2,50000,display_height + gaph + boxb/2 + cgaph,gapv + 0.2*boxl + 3*cgapv + 2*cardh,display_height + gaph + boxb/2 + cgaph,2*gapv + boxl + 0.2*boxl + 3*cgapv + 2*cardh)
            , "hongkong":Property("Hong Kong",new,"China",card_length + 3*(card_breadth/2),display_height - card_length/2,40000,display_height + gaph + boxb/2 + 2*cgaph + cardl,gapv + 0.2*boxl + 3*cgapv + 2*cardh,display_height + gaph + boxb/2 + 2*cgaph + cardl,2*gapv + boxl + 0.2*boxl + 3*cgapv + 2*cardh)
            , "shanghai":Property("Shanghai",new,"China",card_length + 7*(card_breadth/2),display_height - card_length/2,60000,display_height + gaph + boxb/2 + 3*cgaph + 2*cardl,gapv + 0.2*boxl + 3*cgapv + 2*cardh,display_height + gaph + boxb/2 + 3*cgaph + 2*cardl,2*gapv + boxl + 0.2*boxl + 3*cgapv + 2*cardh)
            , "moscow":Property("Moscow",grey,"Russia",display_height - card_length/2,card_length + 13*(card_breadth/2),60000,display_height + gaph + c2gaph,gapv + 0.2*boxl + 4*cgapv + 3*cardh,display_height + gaph + c2gaph,2*gapv + boxl + 0.2*boxl + 4*cgapv + 3*cardh)
            , "saintpetersburg":Property("Saint Petersberg",grey,"Russia",display_height - card_length/2,card_length + 17*(card_breadth/2),40000,display_height + gaph + 2*c2gaph + cardl,gapv + 0.2*boxl + 4*cgapv + 3*cardh,display_height + gaph + 2*c2gaph + cardl,2*gapv + boxl + 0.2*boxl + 4*cgapv + 3*cardh)
            , "capetown":Property("Cape Town",orange,"SouthAfrica",card_length + 13*(card_breadth/2),display_height - card_length/2,80000,display_height + gaph + boxb/2+  c2gaph,gapv + 0.2*boxl + 4*cgapv + 3*cardh,display_height + gaph + boxb/2+ c2gaph,2*gapv + boxl + 0.2*boxl + 4*cgapv + 3*cardh)
            , "durban":Property("Durban",orange,"SouthAfrica",card_length + 17*(card_breadth/2),display_height - card_length/2,60000,display_height + gaph + boxb/2+ 2*c2gaph + cardl,gapv + 0.2*boxl + 4*cgapv + 3*cardh,display_height + gaph + boxb/2+ 2*c2gaph + cardl,2*gapv + boxl + 0.2*boxl + 4*cgapv + 3*cardh)              
            }

        
