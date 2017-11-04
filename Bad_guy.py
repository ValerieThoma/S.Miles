import pygame
from pygame.sprite import Sprite
from math import hypot
from random import randint 

good_guy = pygame.image.load("./images/ghost_sunny.png")


class Bad_guy(Sprite):
	def __init__(self,screen):
		super(Bad_guy,self).__init__()
		self.image = pygame.image.load('./images/ghost_dark.png')
		self.image = pygame.transform.scale(self.image,(75,100))
		self.x = 700
		self.y = 400
		self.screen = screen
		self.speed = 2
		self.rect = self.image.get_rect()

	def update_me(self):
		# dx = self.x #- the_player.x
		# dy = self.y #- the_player.y
		# dist = hypot(dx,dy)
		# dx = dx / dist
		# dy = dy / dist
		# self.x -= dx * self.speed
		# self.y -= dy * self.speed
		self.rect.left = self.x
		self.rect.top = self.y
		self.x -=  self.speed
		self.y +=  self.speed


	def draw_me(self):
		self.rect.left = self.x
		self.rect.top = self.y
		self.screen.blit(self.image,[self.x,self.y])

	def keep_on_screen(self):
		if self.y < 0:
			self.y = 730
		elif self.y > 730:
			self.y = 0
		if self.x < 0:
			self.x = 1000
				
		
	def up_and_away(self):
		self.rect.left = self.x
		self.rect.top = self.y
		self.x =  400
		self.y =  100
		self.speed = 0
		self.image = pygame.transform.scale(good_guy,(95,100))
		