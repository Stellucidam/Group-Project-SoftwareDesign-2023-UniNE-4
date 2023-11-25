import pygame
import random 

WHITE = (255, 255, 255) # defining some general variables that almost all games have...
WINDOWWIDTH = 500
WINDOWHEIGHT = 400
BLOCKING = 3
PANGOLINAREA = 60

windowsurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) # initializes a window for display on the left
clock = pygame.time.Clock() # creates an object that helps track time
score = 0  # declaring a starting score for the game

pygame.init() # initializes all imported pygame modules
pygame.mouse.set_visible(False) # hides the cursor in the game window
pygame.display.set_caption("Save the pangolins") # sets the title for the game window
myfont = pygame.font.SysFont("Verdana", 25, bold = True) # using a pygame font to display a score
background = pygame.image.load("pan_background.png") # loads new images from local files
sarscov2 = pygame.image.load("virus1.png") 
sars = pygame.image.load("virus2.png")
mers = pygame.image.load("virus3.png")
covalt = pygame.image.load("virus4.png")
playerimage = pygame.image.load("mask.png")
player = {"image": playerimage, "rect": playerimage.get_rect()} # a rect is simply a rectangle with some attributes
viruses = []

def virus_behavior():
  virus["rect"].move_ip(virus["speed"]) # moves a rect object in place according to an x and y speed
  if virus["rect"].top < 0: # if the virus rect hits the top of the screen...
    virus["speed"][1] = -virus["speed"][1]
    virus["speed"][0] = random.uniform(-4, 4)
  elif virus["rect"].left < 0 or virus["rect"].right > WINDOWWIDTH: # if the virus rect hits the sides of the screen...
    virus["speed"][0] = -virus["speed"][0]
  elif virus["rect"].bottom > WINDOWHEIGHT - PANGOLINAREA: # if the virus rect hits the pangolins a the bottom of the screen...
    virus["dead"] = True

while True: #THIS OUTER LOOP IS THE GAME LOOP
  if BLOCKING >= 3: # if true this creates a virus dictionary with 4 keys: dead, rect, speed and image
    virus = {"dead": False, 
             "rect": sars.get_rect(center=(random.uniform(60, WINDOWWIDTH-60), 60)),   
             "speed": [random.uniform(-3,3), 2], 
             "image": random.choice([sarscov2, sars, mers, covalt])}
    viruses.append(virus)
    BLOCKING = 0
  
  for event in pygame.event.get(): #pygame module for interacting with events that gets events from the que
    if event.type == pygame.MOUSEMOTION: # if there is mouse motion...
      player["rect"].centerx = event.pos[0] # move the player where the cursor is on the screen
      player["rect"].centery = event.pos[1]
    if event.type == pygame.MOUSEBUTTONDOWN: #if the event is a click with the mouse
      for virus in viruses:  
        if virus["rect"].colliderect(player["rect"]):  #collition detection checking if the playerrect is inside a rect of the virus
          virus["speed"] = [random.uniform(-4, 4), -2] #inverts the virus' speed on the y-axis (creates a bounce)
          BLOCKING +=1
          break

  score += 0.5
  windowsurface.blit(background, (0, 0))  #blit draws one image onto another and its position on the screen 
  scoretext = myfont.render("Pangolins Saved: {0}".format(score), 1, WHITE) #draws text on new surface
  windowsurface.blit(scoretext, (30, 30))
  windowsurface.blit(player["image"], player["rect"])

  for count, virus in enumerate(viruses):
    if not virus["dead"]: # if the virus is not dead
      windowsurface.blit(virus["image"], virus["rect"]) # draws the image of the virus and its position on the screen
    virus_behavior()  # calls the function that determines the behavior/rules of the virus
    if virus["dead"]: # if the virus dies (not caught by the player)
      del viruses[count] # deletes that virus from the virus list
      if virus["image"] == sarscov2: #if the virus is covid it cost more points
        score -= (100 * count)
      score -= (20 * count)

  if score < 0 or len(viruses) == 0: 
    windowsurface.blit(background, (0, 0))
    scoretext = myfont.render("GAME OVER!!!", 1, WHITE)
    windowsurface.blit(scoretext, (150, 150))
    pygame.display.flip() #updates the full display surface to the screen
    break  #breaks the game loop and ends the game

  pygame.display.flip() #updates the full display surface to the screen
  clock.tick(60) #updates the clock and computes how many milliseconds have passed since the previous call