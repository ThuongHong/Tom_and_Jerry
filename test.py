import pygame, sys
import os

class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.sprites = []
		folder_down = r'./Graphics/Tom/Down'
		for file in os.listdir(folder_down):
			self.sprites.append(pygame.image.load(folder_down + '/' + file))
		self.attack_animation = False
		self.current_sprite = 0
		self.image = pygame.image.load(r'./Graphics/Tom/stay.png')

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def attack(self):
		self.attack_animation = True

	def update(self,speed, move):
		if self.attack_animation == True:
			self.current_sprite += speed
			self.rect.topleft = self.rect.topleft + move
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.attack_animation = False
			self.image = self.sprites[int(self.current_sprite)]
		else:
			self.image = pygame.image.load(r'./Graphics/Tom/stay.png')

# General setup
pygame.init()
grid = 30
clock = pygame.time.Clock()
# Game Screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(0,30)
moving_sprites.add(player)
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			player.attack()

	# Drawing
	screen.fill((0,0,0))
	moving_sprites.draw(screen)
	move = pygame.math.Vector2(0,1)
	moving_sprites.update(8/grid, move)
	pygame.display.flip()
	clock.tick(60)