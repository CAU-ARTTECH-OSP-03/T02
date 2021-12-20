#Importing all the modules
try:
    import time, random, sys, os, math
except ImportError:
    print("Make sure to have the time module")
    sys.exit()
try:
    import pygame
except ImportError:
    print("Make sure you have python 3 and pygame.")
    sys.exit()
try:

    from MBTI_Ninja import MainMenu
except ImportError:
    print("Make sure you have all the extra files")
from pygame import freetype


#game_font = pygame.freetype.Font("Font.ttf", 75)
#text_surface, rect = game_font.render(("Programmer: 8BitToaster"), (0, 0, 0))
#gameDisplay.blit(text_surface, (150, 300))

# Initialize the game engine


pygame.init()

DisplayWidth,DisplayHeight = 1000, 800
gameDisplay = pygame.display.set_mode((DisplayWidth,DisplayHeight))
pygame.display.set_caption("Name")

clock = pygame.time.Clock()


#Loading the images
def load_images(mbti, path_to_directory):

    if mbti == 7 :
        obj = 'istj'
        
    elif mbti == 1:
        obj = 'infj'

    elif mbti == 3:
        obj = 'intj'

    elif mbti == 6:
        obj = 'istp'

    elif mbti == 4:
        obj = 'isfp'

    elif mbti == 0:
        obj = 'infp'

    elif mbti == 2:
        obj = 'intp'

    elif mbti == 5:
        obj = 'isfj'

    elif mbti == 14:
        obj = 'estp'

    elif mbti == 12:
        obj = 'esfp'

    elif mbti == 8:
        obj = 'enfp'

    elif mbti == 10:
        obj = 'entp'

    elif mbti == 15:
        obj = 'estj'

    elif mbti == 13:
        obj = 'esfj'

    elif mbti == 9:
        obj = 'enfj'

    elif mbti == 11:
        obj = 'entj'
        
    images = {}
    for dirpath, dirnames, filenames in os.walk(path_to_directory):
        for name in filenames:
            if name.endswith('.png'):
                key = name[:-4]
                if key != "Bg" and (name.startswith(obj) or name.startswith('_')):
                    img = pygame.image.load(os.path.join(dirpath, name)).convert_alpha()
                else:
                    img = pygame.image.load(os.path.join(dirpath, name)).convert()
                images[key] = img
    return images


#Calculates and draws everything for the fruits
class Fruit():
    def __init__(self, Image, x=None, y=None, Vx=None, gravity=None, width=200,height=200):
        """Declares all the starting Variables."""
        self.Image = Image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.Vx = Vx
        self.gravity = gravity
        if x == None:
            self.x = 500
        if y == None:
            self.y = 800
        if Vx == None:
            self.Vx = random.randint(-20,20)
        if gravity == None:
            self.gravity = random.randint(-22,-20)
        self.image = pygame.Surface([self.width,self.height])
        self.rect = self.image.get_rect()
        self.rect.top = self.y
        self.rect.bottom = self.y + self.height
        self.rect.left = self.x
        self.rect.right = self.x + self.width
        self.angle = random.randint(0,355)
        self.split = False
 

    def draw(self):
        """Draws the Fruit."""
        gameDisplay.blit(pygame.transform.rotate(pygame.transform.scale(self.Image,(self.width,self.height)),self.angle).convert_alpha(),(self.x,self.y))

    def Physics(self):
        """Calculates the physics and angles of each fruit."""
        self.x += self.Vx
        self.y += self.gravity
        self.gravity += 0.35
        if self.Vx > 0:
            self.Vx -= 0.25
        if self.Vx < 0:
            self.Vx += 0.25
        if self.x + self.width >= 1000 or self.x <= 0:
            self.Vx *= -1

        #Updating the angles
        self.angle += 1
        self.angle %= 360

    def update(self):
        """Calls every function to update each fruit."""
        self.draw()
        self.Physics()
        #Updating the hitbox
        self.rect.top = self.y
        self.rect.bottom = self.y + self.height
        self.rect.left = self.x
        self.rect.right = self.x + self.width

class Player():
    def __init__(self):
        """Declaring a bunch of variables"""
        pos = pygame.mouse.get_pos()
        self.x = pos[0]
        self.y = pos[1]
        self.width = 5
        self.height = 5
        self.image = pygame.Surface([self.width,self.height])
        self.rect = self.image.get_rect()
        self.rect.top = self.y
        self.rect.bottom = self.y + self.height
        self.rect.left = self.x
        self.rect.right = self.x + self.width
        self.drag = False
        self.Past = []

    def draw(self, Colors):
        """Draws your slashy line"""
        pygame.draw.rect(gameDisplay,(0,255,0),(self.x,self.y,self.width,self.height),0)
        #New Version
        for i in range(len(self.Past)-2):
            self.Past[i][1] -= 1
            if self.Past[i][1] >= 1:
                pygame.draw.line(gameDisplay, Colors[1],(self.Past[i][0]),(self.Past[i+1][0]),self.Past[i][1]+10)
                pygame.draw.line(gameDisplay, Colors[0],(self.Past[i][0]),(self.Past[i+1][0]),self.Past[i][1])
        #Old Version
        '''for point in self.Past:
            point[1] -= 1
            if point[1] >= 0:
                pygame.draw.rect(gameDisplay,Colors[0],(point[0][0],point[0][1]-int(point[1]/2),point[2], point[1]),0)
                pygame.draw.rect(gameDisplay,Colors[1],(point[0][0],point[0][1]-int(point[1]/2),point[2], point[1]),5)'''

    def update(self, Colors):
        """Calls every function to update them"""
        self.draw(Colors)
        #Updating the lines
        pos = pygame.mouse.get_pos()
        change = pygame.mouse.get_rel()
        self.Past.insert(0, [pos, (change[1]+10) % 30, (abs(change[0])*3) % 100])
        if len(self.Past) >= 21:
            self.Past.pop(20)
        #Updating the hitbox
        self.x = pos[0]
        self.y = pos[1]
        self.rect.top = self.y
        self.rect.bottom = self.y + self.height
        self.rect.left = self.x
        self.rect.right = self.x + self.width

class Explosion():
    """A Little class that makes an explosion every time you hit a bomb"""
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.Life = 20

    def draw(self, Images):
        gameDisplay.blit(pygame.transform.scale(Images["_Explosions"],(150,150)),(self.x,self.y))

    def update(self, Images):
        self.draw(Images)
        self.x += random.randint(-5,5)
        self.y += random.randint(-5,5)
        self.Life -= 1

def game_loop(mbti,Colors=[(0,255,0),(0,150,0)]):

    
    if mbti == 7 :
        obj = 'istj'
        
    elif mbti == 1:
        obj = 'infj'

    elif mbti == 3:
        obj = 'intj'

    elif mbti == 6:
        obj = 'istp'

    elif mbti == 4:
        obj = 'isfp'

    elif mbti == 0:
        obj = 'infp'

    elif mbti == 2:
        obj = 'intp'

    elif mbti == 5:
        obj = 'isfj'

    elif mbti == 14:
        obj = 'estp'

    elif mbti == 12:
        obj = 'esfp'

    elif mbti == 8:
        obj = 'enfp'

    elif mbti == 10:
        obj = 'entp'

    elif mbti == 15:
        obj = 'estj'

    elif mbti == 13:
        obj = 'esfj'

    elif mbti == 9:
        obj = 'enfj'

    elif mbti == 11:
        obj = 'entj'
        
    game_run = True
    Images = load_images(mbti, "Images")
    Choices = [obj+'1', obj+'2', obj+'3']
    player = Player()
    Fruits = []
    Lives = 3
    score = 0
    
    for i in range(random.randint(2,5)):
        choice = random.choice(Choices)
        if choice == obj+'1': 
            Fruits.append(Fruit(Images[choice],500,800,random.randint(-20,20),random.randint(-22,-20),125,125))
        else:
            Fruits.append(Fruit(Images[choice]))
    if random.randint(1,4) <= 3:
        Bombs = [Fruit(Images["_Bomb"], 500,1000,random.randint(-30,30),-25,100,100)]
    else:
        Bombs = []
    SplitFruit = []
    Explosions = []

    while game_run == True:

        #gameDisplay.fill((210,140,42))
        gameDisplay.blit(pygame.transform.scale(Images["_Bg"],(DisplayWidth,DisplayHeight)),(0,0))
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.drag = True
            if event.type == pygame.MOUSEBUTTONUP:
                player.Past = []
                player.drag = False

        #Drawing the lives
        if Lives > 0:
            for i in range(Lives):
                pygame.draw.rect(gameDisplay,(250,0,0),(25+(i*55),10,50,50),0)
                pygame.draw.rect(gameDisplay,(150,0,0),(25+(i*55),10,50,50),5)
        else:
            MainMenu.HomeScreen(mbti, score)

        #Drawing all the fruit and its sliced counterparts
        stop = False
        for fruit in Fruits:
            fruit.update()
            if fruit.y <= 800:
                stop = True
            if pygame.sprite.collide_rect(player, fruit) == True and player.drag and not fruit.split:
                fruit.Image = Images["_sparkles"]
                fruit.split = True
                Fruits[-1].split = True
                score += 10
        for fruit in Bombs:
            fruit.update()
            if fruit.y <= 800:
                stop = True
            if pygame.sprite.collide_rect(player, fruit) == True and player.drag:
                Explosions.append(Explosion(fruit.x,fruit.y))
                Lives -= 1
                fruit.x = -100
                fruit.y = 900
                
        if stop == False:
            for fruit in Fruits:
                if fruit.split == False:
                    Lives -= 1
            Fruits = []
            for i in range(random.randint(2,5)):
                choice = random.choice(Choices)
                if choice == obj+'1': 
                    Fruits.append(Fruit(Images[choice],500,800,random.randint(-20,20),random.randint(-22,-20),125,125))
                else:
                    Fruits.append(Fruit(Images[choice]))
            if random.randint(1,4) <= 3:
                Bombs = [Fruit(Images["_Bomb"],500,800,random.randint(-40,40),-20,100,100)]
            else:
                Bombs = []
        for explosion in Explosions:
            explosion.update(Images)
            if explosion.Life <= 0:
                Explosions.pop(Explosions.index(explosion))

        #Drawing the slashy thingy
        if player.drag == True:
            player.update(Colors)
                



        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    MainMenu.HomeScreen()

