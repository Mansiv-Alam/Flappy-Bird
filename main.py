import pygame
import random
# Name: Mansiv Alam


# Date: June 6 2024


# Title: Python Culminating Game


# Purpose: to make a flappy bird type game where you win when you get the score of 25


# initialize variables and the window
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BEIGE = (222, 215, 147)
DARKERBEIGE = (199, 198, 118)
CYAN = (83, 180, 206)
TREEGREEN = (99, 227, 115)
TREELIGHTGREEN = (166, 233, 96)
TREEOUTLINE = (78, 205, 101)
LIGHTGREEN = (142, 212, 76)
DARKGREEN = (92, 121, 17)
bg_active_colour = WHITE
win_height = 600
win_width = 800
screen = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("FlappyBird Game!")
font = pygame.font.SysFont('Comic Sans Ms', 32)
font2 = pygame.font.SysFont('Comic Sans Ms', 24)
font3 = pygame.font.SysFont('Comic Sans Ms Bold', 40)

# My files are as small as possible so that they can fit into my screen/game or else the bird will rotate weirdly and
# not continue jumping after a certain y value
Birdpngs = [pygame.image.load("Flappy Bird downflap.png"),
            pygame.image.load("Flappy Bird midflap.png"),
            pygame.image.load("Flappy Bird upflap.png")]
BottomPipe = pygame.image.load("bottomPipe.png")
TopPipe = pygame.image.load("TopPipe.png")
timer = pygame.time.Clock()

# I make a Class for pipes to make multiple pipe objects and input variables here rather than inside the
# main Code for way cleaner code, I also use the pygame module for basic game objects
class Pipes(pygame.sprite.Sprite):
    def __init__(self, imagegiven, x, y, BirdX):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagegiven
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Variables for making the score increase
        self.PassedPipe = False
        self.PipeEnter = False
        self.PipeExit = False
        self.BirdPos = BirdX
        global PipeY
        PipeY = self.rect.y

    def update(self):
        global Score

        # Making the pipes destroy themselves right before they leave the window
        self.rect.x -= PipeSpeed
        if self.rect.x <= 0:
            self.kill()
        global PipeX
        PipeX = self.rect.x
        # Making the score go up after the bird passes through the pipes
        # Checking if it enters between the pipes
        # + 29 because that is when my image starts showing the pixels for my bird
        if self.BirdPos + 29 > self.rect.x and self.PassedPipe == False:
            self.PipeEnter = True
        # Checking if it has exited after being between the pipes
        # add self.rect.x by 52 because that is how many pixels wide the pipe is
        if self.BirdPos + 29 > self.rect.x + 52 and self.PassedPipe == False:
            self.PipeExit = True
        # after checking if the bird both entered and exited the space between the pipes we add 1 to the score
        if self.PipeEnter == True and self.PipeExit == True and self.PassedPipe == False:
            # since there are a pair of pipes this addition runs twice for each time you go through the pipes
            Score += 0.5
            self.PassedPipe = True

def BackGround():
    # Clouds
    pygame.draw.circle(screen, WHITE, (40, 370), 50)
    pygame.draw.circle(screen, WHITE, (120, 390), 50)
    pygame.draw.circle(screen, WHITE, (200, 360), 50)
    pygame.draw.circle(screen, WHITE, (270, 400), 50)
    pygame.draw.circle(screen, WHITE, (340, 390), 50)
    pygame.draw.circle(screen, WHITE, (420, 360), 50)
    pygame.draw.circle(screen, WHITE, (490, 350), 50)
    pygame.draw.circle(screen, WHITE, (560, 390), 50)
    pygame.draw.circle(screen, WHITE, (630, 360), 50)
    pygame.draw.circle(screen, WHITE, (700, 390), 50)
    pygame.draw.circle(screen, WHITE, (780, 360), 50)
    # Trees
    pygame.draw.circle(screen, TREEGREEN, (80, 430), 30)
    pygame.draw.circle(screen, TREEOUTLINE, (80, 430), 30, 3)
    pygame.draw.circle(screen, TREEGREEN, (20, 430), 40)
    pygame.draw.circle(screen, TREEOUTLINE, (20, 430), 40, 3)
    pygame.draw.circle(screen, TREELIGHTGREEN, (70, 450), 30)
    pygame.draw.circle(screen, TREEOUTLINE, (70, 450), 30, 3)
    pygame.draw.circle(screen, TREEGREEN, (180, 420), 30)
    pygame.draw.circle(screen, TREEOUTLINE, (180, 420), 30, 3)

    pygame.draw.circle(screen, TREELIGHTGREEN, (215, 447), 42)
    pygame.draw.circle(screen, TREEOUTLINE, (215, 447), 42, 3)
    pygame.draw.circle(screen, TREEGREEN, (135, 455), 40)
    pygame.draw.circle(screen, TREEOUTLINE, (135, 455), 40, 3)
    pygame.draw.circle(screen, TREEGREEN, (330, 450), 40)
    pygame.draw.circle(screen, TREEOUTLINE, (330, 450), 40, 3)
    pygame.draw.circle(screen, TREEGREEN, (270, 460), 30)
    pygame.draw.circle(screen, TREEOUTLINE, (270, 460), 30, 3)

    pygame.draw.circle(screen, TREEGREEN, (420, 425), 40)
    pygame.draw.circle(screen, TREEOUTLINE, (420, 425), 40, 3)
    pygame.draw.circle(screen, TREEGREEN, (470, 415), 30)
    pygame.draw.circle(screen, TREEOUTLINE, (470, 415), 30, 3)
    pygame.draw.circle(screen, TREELIGHTGREEN, (390, 445), 30)
    pygame.draw.circle(screen, TREEOUTLINE, (390, 445), 30, 3)
    pygame.draw.circle(screen, TREEGREEN, (510, 435), 40)
    pygame.draw.circle(screen, TREEOUTLINE, (510, 435), 40, 3)
    pygame.draw.circle(screen, TREEGREEN, (450, 450), 35)
    pygame.draw.circle(screen, TREEOUTLINE, (450, 450), 35, 3)

    pygame.draw.circle(screen, TREEGREEN, (655, 435), 40)
    pygame.draw.circle(screen, TREEOUTLINE, (655, 435), 40, 3)
    pygame.draw.circle(screen, TREEGREEN, (610, 440), 35)
    pygame.draw.circle(screen, TREEOUTLINE, (610, 440), 35, 3)
    pygame.draw.circle(screen, TREELIGHTGREEN, (565, 450), 30)
    pygame.draw.circle(screen, TREEOUTLINE, (565, 450), 30, 3)

    pygame.draw.circle(screen, TREELIGHTGREEN, (740, 425), 30)
    pygame.draw.circle(screen, TREEOUTLINE, (740, 425), 30, 3)
    pygame.draw.circle(screen, TREEGREEN, (710, 450), 30)
    pygame.draw.circle(screen, TREEOUTLINE, (710, 450), 30, 3)
    pygame.draw.circle(screen, TREEGREEN, (775, 440), 42)
    pygame.draw.circle(screen, TREEOUTLINE, (775, 440), 42, 3)
    # Ground
    pygame.draw.rect(screen, BEIGE, (0, 510, 800, 90))
    pygame.draw.rect(screen, LIGHTGREEN, (0, 465, 800, 40))
    pygame.draw.line(screen, DARKERBEIGE, (0, 510), (800, 510), 5)
    pygame.draw.line(screen, DARKGREEN, (0, 505), (800, 505), 5)
    pygame.draw.line(screen, DARKERBEIGE, (0, 465), (800, 465), 3)
    pygame.draw.line(screen, DARKGREEN, (0, 462), (800, 462), 5)
def BackGroundFar():
    # Clouds
    pygame.draw.circle(screen, WHITE, (40, 370), 50)
    pygame.draw.circle(screen, WHITE, (120, 390), 50)
    pygame.draw.circle(screen, WHITE, (200, 360), 50)
    pygame.draw.circle(screen, WHITE, (270, 400), 50)
    pygame.draw.circle(screen, WHITE, (340, 390), 50)
    pygame.draw.circle(screen, WHITE, (420, 360), 50)
    pygame.draw.circle(screen, WHITE, (490, 350), 50)
    pygame.draw.circle(screen, WHITE, (560, 390), 50)
    pygame.draw.circle(screen, WHITE, (630, 360), 50)
    pygame.draw.circle(screen, WHITE, (700, 390), 50)
    pygame.draw.circle(screen, WHITE, (780, 360), 50)
    # Trees
    pygame.draw.circle(screen, TREEGREEN, (80, 430), 30)
    pygame.draw.circle(screen, TREEOUTLINE, (80, 430), 30, 3)
    pygame.draw.circle(screen, TREEGREEN, (20, 430), 40)
    pygame.draw.circle(screen, TREEOUTLINE, (20, 430), 40, 3)
    pygame.draw.circle(screen, TREELIGHTGREEN, (70, 450), 30)
    pygame.draw.circle(screen, TREEOUTLINE, (70, 450), 30, 3)
    pygame.draw.circle(screen, TREEGREEN, (180, 420), 30)
    pygame.draw.circle(screen, TREEOUTLINE, (180, 420), 30, 3)

    pygame.draw.circle(screen, TREELIGHTGREEN, (215, 447), 42)
    pygame.draw.circle(screen, TREEOUTLINE, (215, 447), 42, 3)
    pygame.draw.circle(screen, TREEGREEN, (135, 455), 40)
    pygame.draw.circle(screen, TREEOUTLINE, (135, 455), 40, 3)
    pygame.draw.circle(screen, TREEGREEN, (330, 450), 40)
    pygame.draw.circle(screen, TREEOUTLINE, (330, 450), 40, 3)
    pygame.draw.circle(screen, TREEGREEN, (270, 460), 30)
    pygame.draw.circle(screen, TREEOUTLINE, (270, 460), 30, 3)

    pygame.draw.circle(screen, TREEGREEN, (420, 425), 40)
    pygame.draw.circle(screen, TREEOUTLINE, (420, 425), 40, 3)
    pygame.draw.circle(screen, TREEGREEN, (470, 415), 30)
    pygame.draw.circle(screen, TREEOUTLINE, (470, 415), 30, 3)
    pygame.draw.circle(screen, TREELIGHTGREEN, (390, 445), 30)
    pygame.draw.circle(screen, TREEOUTLINE, (390, 445), 30, 3)
    pygame.draw.circle(screen, TREEGREEN, (510, 435), 40)
    pygame.draw.circle(screen, TREEOUTLINE, (510, 435), 40, 3)
    pygame.draw.circle(screen, TREEGREEN, (450, 450), 35)
    pygame.draw.circle(screen, TREEOUTLINE, (450, 450), 35, 3)

    pygame.draw.circle(screen, TREEGREEN, (655, 435), 40)
    pygame.draw.circle(screen, TREEOUTLINE, (655, 435), 40, 3)
    pygame.draw.circle(screen, TREEGREEN, (610, 440), 35)
    pygame.draw.circle(screen, TREEOUTLINE, (610, 440), 35, 3)
    pygame.draw.circle(screen, TREELIGHTGREEN, (565, 450), 30)
    pygame.draw.circle(screen, TREEOUTLINE, (565, 450), 30, 3)

    pygame.draw.circle(screen, TREELIGHTGREEN, (740, 425), 30)
    pygame.draw.circle(screen, TREEOUTLINE, (740, 425), 30, 3)
    pygame.draw.circle(screen, TREEGREEN, (710, 450), 30)
    pygame.draw.circle(screen, TREEOUTLINE, (710, 450), 30, 3)
    pygame.draw.circle(screen, TREEGREEN, (775, 440), 42)
    pygame.draw.circle(screen, TREEOUTLINE, (775, 440), 42, 3)
def BackGroundClose():
    # Ground
    pygame.draw.rect(screen, BEIGE, (0, 510, 800, 90))
    pygame.draw.rect(screen, LIGHTGREEN, (0, 465, 800, 40))
    pygame.draw.line(screen, DARKERBEIGE, (0, 510), (800, 510), 5)
    pygame.draw.line(screen, DARKGREEN, (0, 505), (800, 505), 5)
    pygame.draw.line(screen, DARKERBEIGE, (0, 465), (800, 465), 3)
    pygame.draw.line(screen, DARKGREEN, (0, 462), (800, 462), 5)

def spawnPipes():
    TopPipeX = 700
    BottomPipeX = 700
    # Randomize the height of the pipes + must be negative so that we can take off parts of the png which is
    # The beginning of the pipe and not the end part
    TopPipeY = random.randrange(-700, -491)
    # Making the bottom pipe and a randomized space for the gap using the random height taken off from the top pipe
    # + making the bottom pipe fit into my screen
    BottomPipeY = random.randrange(100, 141) + TopPipeY + BottomPipe.get_height()

    return TopPipeX, TopPipeY, BottomPipeX, BottomPipeY

# Variables for my game
spawnTimer = 0
GameCondition = 1
Score = 0
PipeSpeed = 3
running = True
# Bird Variables
BirdPosition = (350, 250)
Imagenum = 0
BirdAlive = True
BirdisJumping = False
BirdGrav = 0
BirdPosy = BirdPosition[1]
BirdPosx = BirdPosition[0]

# A Group because there will be multiple pipes on the screen
pipes = pygame.sprite.Group()
while running:

    screen.fill(CYAN)
    # Background
    BackGround()
    # Main menu screen
    if GameCondition == 1:
        # Draw the Play button
        playtext = font.render("Play", True, WHITE)
        playtextRect = playtext.get_rect()
        playtextRect.center = (400, 175)
        screen.blit(playtext, playtextRect)
        # Draw the Credits Button
        creditText = font.render("Credits", True, WHITE)
        creditTextRect = creditText.get_rect()
        creditTextRect.center = (400, 220)
        screen.blit(creditText, creditTextRect)
        # Draw the Quit button
        QuitText = font.render("Quit", True, WHITE)
        QuitTextRect = QuitText.get_rect()
        QuitTextRect.center = (400, 260)
        screen.blit(QuitText, QuitTextRect)
        # Get mouse clicks and mouse position (Input)
        MouseClick = pygame.mouse.get_pressed()
        Mousepos = pygame.mouse.get_pos()
        Mouseposx = Mousepos[0]
        Mouseposy = Mousepos[1]
        # Make a hitbox for the Play button (Process)
        if MouseClick[0] == True and Mouseposx > 365 and Mouseposx < 435:
            if Mouseposy > 163 and Mouseposy < 205:
                GameCondition = 2
        if MouseClick[0] == True and Mouseposx > 340 and Mouseposx < 460:
            if Mouseposy > 205 and Mouseposy < 240:
                GameCondition = 3
        if MouseClick[0] == True and Mouseposx > 363 and Mouseposx < 440:
            if Mouseposy > 245 and Mouseposy < 285:
                running = False
    # Credits screen
    elif GameCondition == 3:
        # programmer text Output
        programmerText = font.render("Programmers:", True, WHITE)
        programmerTextRect = programmerText.get_rect()
        programmerTextRect.center = (400, 50)
        screen.blit(programmerText, programmerTextRect)
        NameText = font2.render("Mansiv Alam", True, WHITE)
        NameTextRect = NameText.get_rect()
        NameTextRect.center = (400, 85)
        screen.blit(NameText, NameTextRect)
        # sound design text Output
        soundText = font.render("Sound Design:", True, WHITE)
        soundTextRect = soundText.get_rect()
        soundTextRect.center = (400, 125)
        screen.blit(soundText, soundTextRect)
        Name2Text = font2.render("Mansiv Alam", True, WHITE)
        Name2TextRect = Name2Text.get_rect()
        Name2TextRect.center = (400, 155)
        screen.blit(Name2Text, Name2TextRect)
        # Producer text Output
        producerText = font.render("Producer:", True, WHITE)
        producerTextRect = producerText.get_rect()
        producerTextRect.center = (400, 195)
        screen.blit(producerText, producerTextRect)
        Name3Text = font2.render("Mansiv Alam", True, WHITE)
        Name3TextRect = Name3Text.get_rect()
        Name3TextRect.center = (400, 220)
        screen.blit(Name3Text, Name3TextRect)
        # Lead designer text Output
        leadDesignerText = font.render("Lead Designer:", True, WHITE)
        leadDesignerTextRect = leadDesignerText.get_rect()
        leadDesignerTextRect.center = (400, 255)
        screen.blit(leadDesignerText, leadDesignerTextRect)
        Name4Text = font2.render("Mansiv Alam", True, WHITE)
        Name4TextRect = Name4Text.get_rect()
        Name4TextRect.center = (400, 290)
        screen.blit(Name4Text, Name4TextRect)
        # Draw Exit button Output
        ExitText = font.render("Exit", True, WHITE)
        ExitTextRect = ExitText.get_rect()
        ExitTextRect.center = (50, 30)
        screen.blit(ExitText, ExitTextRect)
        # Name, Date, Class Code (Output)
        InfoText = font2.render("Mansiv Alam", True, WHITE)
        InfoTextRect = InfoText.get_rect()
        InfoTextRect.center = (700, 30)
        screen.blit(InfoText, InfoTextRect)
        InfoText = font2.render("June 14 2024", True, WHITE)
        InfoTextRect = InfoText.get_rect()
        InfoTextRect.center = (700, 60)
        screen.blit(InfoText, InfoTextRect)
        InfoText = font2.render("TEJ201", True, WHITE)
        InfoTextRect = InfoText.get_rect()
        InfoTextRect.center = (700, 90)
        screen.blit(InfoText, InfoTextRect)
        # Get mouse clicks and mouse position to click the exit button (Input)
        MouseClick = pygame.mouse.get_pressed()
        Mousepos = pygame.mouse.get_pos()
        Mouseposx = Mousepos[0]
        Mouseposy = Mousepos[1]
        # Making a hitbox for the exit button (Process)
        if MouseClick[0] == True and Mouseposx > 15 and Mouseposx < 84:
            if Mouseposy > 15 and Mouseposy < 50:
                GameCondition = 1
    # Instruction Screen
    elif GameCondition == 2:
        # Draw Instruction text
        InstructionText = font.render("- Press the Spacebar to Jump", True, WHITE)
        InstructionTextRect = InstructionText.get_rect()
        InstructionTextRect.center = (300, 70)
        screen.blit(InstructionText, InstructionTextRect)
        InstructionText = font.render("- Get a score of 25 to win", True, WHITE)
        InstructionTextRect = InstructionText.get_rect()
        InstructionTextRect.center = (275, 120)
        screen.blit(InstructionText, InstructionTextRect)
        # Click to win text
        InstructionText = font3.render("Click to Start", True, WHITE)
        InstructionTextRect = InstructionText.get_rect()
        InstructionTextRect.center = (400, 250)
        screen.blit(InstructionText, InstructionTextRect)

    # Main Game
    elif GameCondition == 4:

        screen.fill(CYAN)
        BackGroundFar()
        # Process
        if BirdAlive == False:
            # Death screen
            GameCondition = 5
        if Score == 25:
            # Win Screen
            GameCondition = 6

        # Input
        UserInput = pygame.key.get_pressed()

        # Drawing and Updating the bird to animate it / make it jump (Process)
        if BirdAlive == True:
            Imagenum += 1
        if Imagenum >= 30:
            Imagenum = 0

        #Adding Gravity
        BirdGrav += 0.5
        # making terminal velocity
        if BirdGrav > 7:
            BirdGrav = 7
        # Changing the y for the bird so it is affect by the gravity
        if BirdPosy < 500:
            BirdPosy += int(BirdGrav)
        # making it so that we cant jump really quickly by spamming inputs
        if BirdGrav == 0:
            BirdisJumping = False
        # Rotating the Bird towards where it's going
        Birdimages = Birdpngs[Imagenum // 10]
        Birdimages = pygame.transform.rotate(Birdimages, BirdGrav * -1)
        # Drawing the bird
        screen.blit(Birdimages, (BirdPosx, BirdPosy))
        # Making the bird jump with certain conditions
        if UserInput[pygame.K_SPACE] and BirdAlive == True and BirdPosy > 0 and BirdisJumping == False:
            BirdisJumping = True
            BirdGrav = -7

        # Making a timer to spawn pipes periodically
        while spawnTimer <= 0 and BirdAlive == True:
            # returning variables for my pipe instances
            TopX, TopY, BotX2, BotY2 = spawnPipes()
            # Makes a pair of pipes everytime
            pipes.add(Pipes(TopPipe, TopX, TopY, BirdPosx))
            # saves the top pipe y to a variable before the self.rect.y is for the bottom pipe
            pipes.update()
            TopPipeY = PipeY
            pipes.add(Pipes(BottomPipe, BotX2, BotY2, BirdPosx))
            spawnTimer = random.randrange(110, 140)

        # Update the data of the pipes
        pipes.update()
        BottomPipeY = PipeY
        # hitbox for the bird (used some pixel measurements for the parameters)
        BirdRect = pygame.Rect(BirdPosx + 29, BirdPosy + 34, 50, 35)
        # hitbox for the top and bottom pipes
        TopPipeRect = pygame.Rect(PipeX, TopPipeY, TopPipe.get_width(), TopPipe.get_height())
        BottomPipeRect = pygame.Rect(PipeX, BottomPipeY, BottomPipe.get_width(), BottomPipe.get_height())
        # Checks if the bird hit box and pipe hit box overlap and if they do you lose
        if BirdRect.colliderect(TopPipeRect) or BirdRect.colliderect(BottomPipeRect):
            GameCondition = 5
            BirdAlive = False

        spawnTimer -= 1
        # Draw the pipes (Output)
        pipes.draw(screen)
        # Drawing the ground over the pipes so it doesn't look like the pipes are popping out
        BackGroundClose()
        if BirdPosy + 60 > 440:
            BirdAlive = False
        # Score text Output
        ScoreText = font2.render("Score:", True, WHITE)
        ScoreTextRect = ScoreText.get_rect()
        ScoreTextRect.center = (100, 50)
        screen.blit(ScoreText, ScoreTextRect)

        # Variable text Output
        score_str = str(int(Score)) if Score.is_integer() else str(Score)
        ScoreText = font2.render(str(Score), True, WHITE)
        ScoreTextRect = ScoreText.get_rect()
        ScoreTextRect.center = (170, 50)
        screen.blit(ScoreText, ScoreTextRect)
        pygame.display.update()

    # Lose Screen
    elif GameCondition == 5:
        # Game Over text Output
        GameOverText = font3.render("Game Over", True, BLACK)
        GameOverTextRect = GameOverText.get_rect()
        GameOverTextRect.center = (400, 75)
        screen.blit(GameOverText, GameOverTextRect)
        # Restart text Output
        RestartText = font.render("Restart?", True, WHITE)
        RestartTextRect = RestartText.get_rect()
        RestartTextRect.center = (400, 125)
        screen.blit(RestartText, RestartTextRect)
        MouseClick = pygame.mouse.get_pressed()
        Mousepos = pygame.mouse.get_pos()
        Mouseposx = Mousepos[0]
        Mouseposy = Mousepos[1]
        # Score text Output
        ScoreText = font.render("Score:", True, WHITE)
        ScoreTextRect = ScoreText.get_rect()
        ScoreTextRect.center = (100, 50)
        screen.blit(ScoreText, ScoreTextRect)
        # Variable text Output
        ScoreText = font.render(str(Score), True, WHITE)
        ScoreTextRect = ScoreText.get_rect()
        ScoreTextRect.center = (180, 50)
        screen.blit(ScoreText, ScoreTextRect)
        pygame.display.update()
        # Make a hitbox for the replay button
        # Process
        if MouseClick[0] == True and Mouseposx > 330 and Mouseposx < 470:
            if Mouseposy > 110 and Mouseposy < 145:
                GameCondition = 1
                spawnTimer = 0
                Score = 0
                PipeSpeed = 3
                running = True
                # Bird Variables
                BirdPosition = (350, 250)
                Imagenum = 0
                BirdAlive = True
                BirdisJumping = False
                BirdGrav = 0
                BirdPosy = BirdPosition[1]
                BirdPosx = BirdPosition[0]
                pipes.empty()
    # Win Screen
    if GameCondition == 6:
        # You win text Output
        YouWinText = font3.render("YOU WIN!!!", True, WHITE)
        YouWinTextRect = YouWinText.get_rect()
        YouWinTextRect.center = (400, 75)
        screen.blit(YouWinText, YouWinTextRect)
        # Restart text Output
        RestartText = font.render("Restart?", True, WHITE)
        RestartTextRect = RestartText.get_rect()
        RestartTextRect.center = (400, 125)
        screen.blit(RestartText, RestartTextRect)
        MouseClick = pygame.mouse.get_pressed()
        Mousepos = pygame.mouse.get_pos()
        Mouseposx = Mousepos[0]
        Mouseposy = Mousepos[1]
        # Make a hitbox for the replay button
        # Process
        if MouseClick[0] == True and Mouseposx > 330 and Mouseposx < 470:
            if Mouseposy > 110 and Mouseposy < 145:
                GameCondition = 1
                spawnTimer = 0
                Score = 0
                PipeSpeed = 3
                running = True
                # Bird Variables
                BirdPosition = (350, 250)
                Imagenum = 0
                BirdAlive = True
                BirdisJumping = False
                BirdGrav = 0
                BirdPosy = BirdPosition[1]
                BirdPosx = BirdPosition[0]
                pipes.empty()

    timer.tick(60)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # Input/Process
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and GameCondition == 2:
            GameCondition = 4

pygame.quit()