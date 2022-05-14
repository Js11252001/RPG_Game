import pygame
from setting import * 

class UI:
	def __init__(self):
		
		# general 
		self.displaySurface = pygame.display.get_surface()
		self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)

		# bar setup 
		self.healthBarRect = pygame.Rect(10,10,HEALTH_BAR_WIDTH,BAR_HEIGHT)
		self.energyBarRect = pygame.Rect(10,34,ENERGY_BAR_WIDTH,BAR_HEIGHT)

		# convert weapon dictionary
		self.weaponGraphics = []
		for weapon in weaponData.values():
			path = weapon['graphic']
			weapon = pygame.image.load(path).convert_alpha()
			self.weaponGraphics.append(weapon)
		# convert magic dictionary
		self.magicGraphics = []
		for magic in magicData.values():
			magic = pygame.image.load(magic['graphic']).convert_alpha()
			self.magicGraphics.append(magic)


	def showBar(self,current,maxAmount,bgRect,color):
		# draw bg 
		pygame.draw.rect(self.displaySurface,UI_BG_COLOR,bgRect)

		# converting stat to pixel
		ratio = current / maxAmount
		currentWidth = bgRect.width * ratio
		currentRect = bgRect.copy()
		currentRect.width = currentWidth

		# drawing the bar
		pygame.draw.rect(self.displaySurface,color,currentRect)
		pygame.draw.rect(self.displaySurface,UI_BORDER_COLOR,bgRect,3)

	def showExp(self,exp):
		textSurf = self.font.render(str(int(exp)),False,TEXT_COLOR)
		x = self.displaySurface.get_size()[0] - 20
		y = self.displaySurface.get_size()[1] - 20
		textRect = textSurf.get_rect(bottomright = (x,y))

		pygame.draw.rect(self.displaySurface,UI_BG_COLOR,textRect.inflate(20,20))
		self.displaySurface.blit(textSurf,textRect)
		pygame.draw.rect(self.displaySurface,UI_BORDER_COLOR,textRect.inflate(20,20),3)

	def selectionBox(self,left,top, hasSwitched):
		bgRect = pygame.Rect(left,top,ITEM_BOX_SIZE,ITEM_BOX_SIZE)
		pygame.draw.rect(self.displaySurface,UI_BG_COLOR,bgRect)
		if hasSwitched:
			pygame.draw.rect(self.displaySurface,UI_BORDER_COLOR_ACTIVE,bgRect,3)
		else:
			pygame.draw.rect(self.displaySurface,UI_BORDER_COLOR,bgRect,3)
		return bgRect

	def weaponOverlay(self,weapon_index,hasSwitched):
		bgRect = self.selectionBox(10,630,hasSwitched)
		weapon_surf = self.weaponGraphics[weapon_index]
		weaponRect = weapon_surf.get_rect(center = bgRect.center)

		self.displaySurface.blit(weapon_surf,weaponRect)

	def magicOverlay(self,magicIndex,hasSwitched):
		bgRect = self.selectionBox(80,635,hasSwitched)
		magicSurf = self.magicGraphics[magicIndex]
		magicRect = magicSurf.get_rect(center = bgRect.center)

		self.displaySurface.blit(magicSurf,magicRect)

	def display(self,player):
		self.showBar(player.health,player.stats['health'],self.healthBarRect,HEALTH_COLOR)
		self.showBar(player.energy,player.stats['energy'],self.energyBarRect,ENERGY_COLOR)

		self.showExp(player.exp)

		self.weaponOverlay(player.weaponIndex,not player.canSwitchWeapon)
		self.magicOverlay(player.magicIndex,not player.canSwitchMagic)