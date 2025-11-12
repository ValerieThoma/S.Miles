import math
import random
import pygame
from pygame.sprite import Sprite

good_guy = pygame.image.load("./images/ghost_sunny.png")


class Bad_guy(Sprite):
	def __init__(self,screen):
		super(Bad_guy,self).__init__()
		self.image = pygame.image.load('./images/ghost_dark.png')
		self.image = pygame.transform.scale(self.image,(75,100))
		self.x = 700
		self.y = 400
		self.screen = screen
		self.speed = 1.5
		self.rect = self.image.get_rect()
		self.state = "hostile"
		self.float_speed = 3
		self._direction_timer = 0
		self._dx = 0
		self._dy = 0
		self._pick_new_direction()

	def _pick_new_direction(self):
		angle = random.uniform(0, math.tau)
		self._dx = math.cos(angle) * self.speed
		self._dy = math.sin(angle) * self.speed
		self._direction_timer = random.randint(60, 180)  # roughly 1-3 seconds at 60 FPS

	def update_me(self):
		self.rect.left = self.x
		self.rect.top = self.y
		if self.state == "rescued":
			self.y -= self.float_speed
		else:
			if self._direction_timer <= 0:
				self._pick_new_direction()
			self.x += self._dx
			self.y += self._dy
			self._direction_timer -= 1


	def draw_me(self):
		self.rect.left = self.x
		self.rect.top = self.y
		self.screen.blit(self.image,[self.x,self.y])

	def keep_on_screen(self):
		if self.state == "rescued":
			return
		if self.y < 0:
			self.y = 730
		elif self.y > 730:
			self.y = 0
		if self.x < 0:
			self.x = 1000
		elif self.x > 1000:
			self.x = 0

		
	def up_and_away(self):
		self.rect.left = self.x
		self.rect.top = self.y
		self.state = "rescued"
		self.image = pygame.transform.scale(good_guy,(95,100))
		self.rect = self.image.get_rect()
		self.rect.centerx = self.x
		self.rect.centery = self.y
		self._dx = 0
		self._dy = -self.float_speed
		