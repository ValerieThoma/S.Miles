import pygame
from pygame.sprite import groupcollide

from Player import Player
from Bad_guy import Bad_guy
from Bullet import Bullet

MAX_BAD_GUYS = 5
MAX_TOTAL_BAD_GUYS = 15

SCREEN_SIZE = (1000, 730)
BACKGROUND_DEFAULT_PATH = "./images/bg.png"
BACKGROUND_SUNNY_PATH = "./images/bg_sunny.png"
HERO_IMAGE_SUNNY = "./images/hero_sunny.png"
HERO_IMAGE_DARK = "./images/hero_dark.png"

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("S.Miles")

background_default = pygame.image.load(BACKGROUND_DEFAULT_PATH)
background_sunny = pygame.image.load(BACKGROUND_SUNNY_PATH)
current_background = background_default

the_player = Player(HERO_IMAGE_SUNNY, 174, 400, screen)

bad_guys = pygame.sprite.Group()
bad_guys.add(Bad_guy(screen))

bullets = pygame.sprite.Group()

total_bad_guys_spawned = len(bad_guys)
rescued_bad_guys = 0
game_over = False
game_over_surface = None
game_over_rect = None
font = pygame.font.Font(None, 64)

def hostile_count(group):
	return sum(1 for bg in group if getattr(bg, "state", "hostile") == "hostile")

game_on = True
while game_on:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False
		elif event.type == pygame.KEYDOWN:
			print(event.key)
			if event.key == pygame.K_UP:
				the_player.should_move("up", True)
			elif event.key == pygame.K_DOWN:
				the_player.should_move("down", True)
			if event.key == pygame.K_RIGHT:
				the_player.should_move("right", True)
			elif event.key == pygame.K_LEFT:
				the_player.should_move("left", True)
			elif event.key == pygame.K_SPACE and not game_over:
				new_bullet = Bullet(screen, the_player, 1)
				bullets.add(new_bullet)
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				the_player.should_move("up", False)
			elif event.key == pygame.K_DOWN:
				the_player.should_move("down", False)
			if event.key == pygame.K_RIGHT:
				the_player.should_move("right", False)
			elif event.key == pygame.K_LEFT:
				the_player.should_move("left", False)

	screen.blit(current_background, (0, 0))

	for bad_guy in list(bad_guys):
		bad_guy.update_me()
		bad_guy.draw_me()
		bad_guy.keep_on_screen()

	the_player.draw_me()
	the_player.keep_on_screen()

	for bullet in list(bullets):
		bullet.update()
		bullet.draw_bullet()

	bullet_hit = groupcollide(bullets, bad_guys, True, False)
	if bullet_hit:
		for hit_list in bullet_hit.values():
			for hit_bad_guy in hit_list:
				if getattr(hit_bad_guy, "state", "hostile") == "hostile":
					hit_bad_guy.up_and_away()
					rescued_bad_guys += 1
					if (
						not game_over
						and hostile_count(bad_guys) < MAX_BAD_GUYS
						and total_bad_guys_spawned < MAX_TOTAL_BAD_GUYS
					):
						bad_guys.add(Bad_guy(screen))
						total_bad_guys_spawned += 1

	if (
		not game_over
		and hostile_count(bad_guys) == 0
		and total_bad_guys_spawned >= MAX_TOTAL_BAD_GUYS
	):
		game_over = True
		current_background = background_sunny
		the_player.set_image(HERO_IMAGE_DARK)
		game_over_surface = font.render("All friends are safe!", True, (255, 255, 255))
		game_over_rect = game_over_surface.get_rect(
			center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2)
		)

	if game_over and game_over_surface:
		screen.blit(game_over_surface, game_over_rect)

	pygame.display.flip()

