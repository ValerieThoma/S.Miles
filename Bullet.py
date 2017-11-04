import pygame
from pygame.sprite import Sprite
import random 
from random import randint 

class Bullet(Sprite):
	def __init__(self,screen,the_player,direction):
		super(Bullet, self).__init__()
		self.screen = screen
		self.rect = pygame.Rect(0,0,0,5)
		self.color = (0,0,0)
		self.rect.centerx = (the_player.x + 40)
		self.rect.top = (the_player.y + 100)
		self.speed = 15
		self.direction = 2
		self.x = self.rect.x
		self.y = self.rect.y
		self.images = cupcake_img
		self.image = pygame.transform.scale(self.images,(35,35))

		

	def update(self):
		if self.direction == 1: #up
			self.y -= self.speed #change the y, each time update is run, by bullet speed
			self.rect.y = self.y #update rect position
		elif self.direction == 2: #right
			self.x += self.speed #change the y, each time update is run, by bullet speed
			self.rect.x = self.x #update rect position
		elif self.direction == 3: #down
			self.y += self.speed #change the y, each time update is run, by bullet speed
			self.rect.y = self.y #update rect position
		else: #left
			self.x -= self.speed #change the y, each time update is rufn, by bullet speed
			self.rect.x = self.x #update rect position


	def draw_bullet(self):
		self.screen.blit(self.image, [self.x,self.y])
		# pygame.draw.rect(self.screen, self.image, self.rect) #draw the bullet!
	
	


cookie_img = pygame.image.load("./images/cookie.png")
cupcake_img = pygame.image.load("./images/cupcake.png")
doughnut_img = pygame.image.load("./images/doughnut.png")
icecream_img = pygame.image.load("./images/icecream.png")

