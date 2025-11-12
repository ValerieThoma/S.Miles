import pygame
from pygame.sprite import Sprite

cookie_img = pygame.image.load("./images/cookie.png")
cupcake_img = pygame.image.load("./images/cupcake.png")
doughnut_img = pygame.image.load("./images/doughnut.png")
icecream_img = pygame.image.load("./images/icecream.png")

DEFAULT_BULLET_SPEED = 4

class Bullet(Sprite):
	_image_cycle = [cookie_img, cupcake_img, doughnut_img, icecream_img]
	_cycle_index = 0

	def __init__(self,screen,the_player,direction):
		super(Bullet, self).__init__()
		self.screen = screen
		self.rect = pygame.Rect(0,0,35,35)
		self.rect.centerx = the_player.x + 40
		self.rect.top = the_player.y + 100
		self.speed = DEFAULT_BULLET_SPEED
		self.direction = direction
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		self.image = pygame.transform.scale(self._next_image(),(35,35))

	@classmethod
	def _next_image(cls):
		image = cls._image_cycle[cls._cycle_index]
		cls._cycle_index = (cls._cycle_index + 1) % len(cls._image_cycle)
		return image

	def update(self):
		if self.direction == 1: #up
			self.y -= self.speed #change the y, each time update is run, by bullet speed
			self.rect.y = int(self.y) #update rect position
		elif self.direction == 2: #right
			self.x += self.speed #change the y, each time update is run, by bullet speed
			self.rect.x = int(self.x) #update rect position
		elif self.direction == 3: #down
			self.y += self.speed #change the y, each time update is run, by bullet speed
			self.rect.y = int(self.y) #update rect position
		else: #left
			self.x -= self.speed #change the y, each time update is run, by bullet speed
			self.rect.x = int(self.x) #update rect position


	def draw_bullet(self):
		self.screen.blit(self.image, [self.rect.x,self.rect.y])

