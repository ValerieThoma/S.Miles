# Rob's notes are the best! 
# We have access to pygame, because we did:
# $ pip install pygame
# it is NOT part of core. This is a 3rd party module.
import pygame
from pygame.sprite import Group, groupcollide
import random
from random import randint  
import time  # I imported this but haven't used it yet. I think I should probably use it, what do you think?


# -----CUSTOM CLASSES HERE-----
from Player import Player
from Bad_guy import Bad_guy
from Bullet import Bullet

# Have to init the pygame object so we can use it
pygame.init()

# Screen size is a tuple
screen_size = (1000,730)
# Because we are going to paint the background, we need a tuple for the color
background_image = pygame.image.load("./images/bg.png")
# start_screen = pygame.image.load("./images/home_screen.png")

# Create a screen for pygame to use to draw on
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("S.Miles")

the_player = Player('./images/hero_sunny.png',100,100,screen)
# Make a bad_guy
bad_guy = Bad_guy(screen)
# make a group for the bad_guys
# bad_guys = Group()
bad_guys = pygame.sprite.Group()

bad_guys.add(bad_guy)##adding ghost to screen!important!
# ghost2 = Bad_guy(screen)
# ghost3 = Bad_guy(screen)
# ghost4 = Bad_guy(screen)
# ghost5 = Bad_guy(screen)
# bad_guys.add(ghost2)
# bad_guys.add(ghost3)
# bad_guys.add(ghost4)
# bad_guys.add(ghost5)



good_guy = pygame.image.load("./images/ghost_sunny.png")

# Make a new Group called bullets. Group is a pygame "list"
#Loading all the "bullet" items.
cookie_img = pygame.image.load("./images/cookie.png")
cupcake_img = pygame.image.load("./images/cupcake.png")
doughnut_img = pygame.image.load("./images/doughnut.png")
icecream_img = pygame.image.load("./images/icecream.png")
# cookie_img = Bullet(screen,the_player,the_player.x)
# cupcake_img = Bullet(screen,the_player,the_player.x)
bullets = pygame.sprite.Group()
# bullets.add(cookie_img)  ###THIS  DOESN'T WORK! HOW CAN I HAVE UNIQUE 'BULLETS?' ARRAY? I think I need a list.
# bullets.add(icecream_img)
# bullets.add(doughnut_img)


game_on = True;
# Set up the main game loop
while game_on: #will run forever (until break)
	# Loop through all the pygame events.
	# This is pygame's escape hatch. (Quit)
	for event in pygame.event.get():
		# print event
		if event.type == pygame.QUIT:
			game_on = False
		elif event.type == pygame.KEYDOWN:
			print event.key
			# print "User pressed a key!!!"
			if event.key == 273:
				# user pressed up!
				# the_player.y -= the_player.speed
				the_player.should_move("up",True)
			elif event.key == 274:
				# the_player.y += the_player.speed
				the_player.should_move("down",True)
			if event.key == 275:
				# the_player.x += the_player.speed
				the_player.should_move("right",True)
			elif event.key == 276:
				# the_player.x -= the_player.speed
				the_player.should_move("left",True)
			elif event.key == 32:
				# 32 = SPACE BAR... FIRE!!!!
				new_bullet = Bullet(screen, the_player, 1)
				bullets.add(new_bullet)
		elif event.type == pygame.KEYUP:
			if event.key == 273:
				the_player.should_move("up",False)
			elif event.key == 274:
				the_player.should_move("down",False)
			if event.key == 275:
				the_player.should_move("right",False)
			elif event.key == 276:
				the_player.should_move("left",False)

	screen.blit(background_image, [0,0]);

	for bad_guy in bad_guys:
		# update the bad guy (based on where the player is)
		bad_guy.update_me()
		# draw the bad guy
		bad_guy.draw_me()


	# # Must be after fill, or we won't be able to see the hero
	# screen.blit(the_player.image, [the_player.x,the_player.y])
	the_player.draw_me()
	the_player.keep_on_screen()
	bad_guy.keep_on_screen()



	for bullet in bullets:
		# update the bullet location
		bullet.update()
		# draw the bullet on the screen
		bullet.draw_bullet()
		# bullet.bullet_randomization()
	

	# Check for collions...
	bullet_hit = groupcollide(bullets,bad_guys,True,False)
	if (bullet_hit):
		bad_guys.add(Bad_guy(screen))
		# bad_guy.image = pygame.transform.scale(good_guy,(95,100))
		bad_guy.up_and_away()


	
		


	 # a bunch of failed logic		
	# if len(bad_guys) == 0:
		# bad_guys.add(Bad_guy(screen))
		
	# if len(bullets) == 0:
	# 	bullets.add(Bullet(screen))
	
	# print bullet_hit

	# flip the screen, i.e.clear it so we can draw again... and again... and again
	pygame.display.flip()






	
###############################################
# WHAT I WANT/HOW I WANT MY BULLETS TO BEHAVE #

# 1. LOAD IMAGES (4 DIFFERENT IMAGES) TO A GROUP OR LIST OR "SOMETHING"
# 2. EACH TIME THE USER PRESSES SPACE BAR/32, THE IMAGE GROUP CYCLES THROUGH THE FOUR DIFFERENT IMAGES. 
# --use a for loop to iterate through the group (look at the example from shuffle deck in blackjack game.)
#look up .shuffle or whatever method that Rob mentioned. 

# clock = pygame.time.Clock() ?? Do I need this?



