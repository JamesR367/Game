import pygame
import random

class Game:
    #game varaibles
    def __init__(self):
        self.MaxY = 720
        self.MaxX = 1280
        self.screen = pygame.display.set_mode((self.MaxX, self.MaxY))
        self.clock = pygame.time.Clock()
        self.running = True
        self.Xcord = random.randint(1,1230)
        self.Ycord = random.randint(1,670)
        self.square = pygame.Rect(self.Xcord,self.Ycord,25,25) 
        self.player = pygame.Rect(1,1,25,25)
        self.chaser = pygame.Rect(1,1,25,25)
        self.display_list = []
  
    #shows the game screen and stores the blue object list
    def display(self):
        self.screen.fill("white")
        for i in self.display_list:
            pygame.draw.rect(self.screen, (0, 0, 255), i)

    #takes key input to move the green square
    def Movement(self,keys_pressed):
        VEL = 5
        if keys_pressed[pygame.K_w] and self.player.y > 1:
                self.player.y -= VEL
        if keys_pressed[pygame.K_s]and self.player.y < (self.MaxY-25):
                self.player.y += VEL
        if keys_pressed[pygame.K_a] and self.player.x > 1:
                self.player.x -= VEL
        if keys_pressed[pygame.K_d] and self.player.x < (self.MaxX-25):
                self.player.x += VEL

#when the player runs into the red square it moves to a random position on the screen
    def moveSquare(self):
        Xcord = random.randint(1,1230)
        Ycord = random.randint(1,670)
        self.square.update((Xcord, Ycord), (25, 25))
        if self.square.collidelistall(self.display_list):
            Xcord = random.randint(1,1230)
            Ycord = random.randint(1,670)
            self.square.update((Xcord, Ycord), (25, 25))

#when the player hits the red square it adds a blue square to the list which shows on the screen
    def addObstacle(self):
        ObXCord = random.randint(1,1230)
        ObYCord = random.randint(1,670)
        if self.player.collidelistall(self.display_list):
            ObXCord = random.randint(1,1230)
            ObYCord = random.randint(1,670)    
        self.display_list.append(pygame.Rect(ObXCord, ObYCord, 38, 38))
   
#when the player hits a blue square or the chaser it clears the boared and set the player postion to (0,0) and moves the red square to a random positioin
    def restartGame(self): 
        self.player.update(1,1,25,25)
        self.moveSquare()
        self.display_list.clear()

#Once the player get past 10 blue square the chaser spawns
    def spawnChaser(self):    
        pygame.draw.rect(self.screen,(0,0,0),self.chaser)
        if self.chaser.x > self.player.x:
            self.chaser.x -=1
        elif self.chaser.x < self.player.x:
            self.chaser.x +=1
        if self.chaser.y > self.player.y:
            self.chaser.y -=1
        elif self.chaser.y < self.player.y:
            self.chaser.y +=1
            
    def runGame(self):
        pygame.init()
        while self.running:
            Game.display(self)
            pygame.draw.rect(self.screen,(255,0,0),self.square)
            pygame.draw.rect(self.screen,(0,255,0),self.player)
            keys_pressed = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if self.player.colliderect(self.square):
                Game.addObstacle(self)
                Game.moveSquare(self)
            if self.player.collidelistall(self.display_list):
                Game.restartGame(self)
            if len(self.display_list) > 10:
                Game.spawnChaser(self)
                if self.player.colliderect(self.chaser):
                    Game.restartGame(self)

            
            Game.Movement(self,keys_pressed)
            pygame.display.update()
            
        
            self.clock.tick(60)  

        pygame.quit()