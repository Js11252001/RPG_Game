import pygame
from setting import *
from entity import Entity
from support import *

class Enemy(Entity):
	def __init__(self,monsterName,pos,groups,obstacleSprites):

		# general setup
		super().__init__(groups)
		self.spriteType = 'enemy'

		# graphics setup
		self.importGraphics(monsterName)
		self.status = 'idle'
		self.image = self.animations[self.status][self.frameIndex]

		# movement
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-10)
		self.obstacleSprites = obstacleSprites

		# stats
		self.monsterName = monsterName
		monsterInfo = monsterData[self.monsterName]
		self.health = monsterInfo['health']
		self.exp = monsterInfo['exp']
		self.speed = monsterInfo['speed']
		self.attackDamage = monsterInfo['damage']
		self.resistance = monsterInfo['resistance']
		self.attackRadius = monsterInfo['attack_radius']
		self.noticeRadius = monsterInfo['notice_radius']
		self.attackType = monsterInfo['attack_type']

		# player interaction
		self.canAttack = True
		self.attackTime = None
		self.attackCooldown = 400

	def importGraphics(self,name):
		self.animations = {'idle':[],'move':[],'attack':[]}
		mainPath = f'./graphics/monsters/{name}/'
		for animation in self.animations.keys():
			self.animations[animation] = importFolder(mainPath + animation)

	def getPlayerDistanceDirection(self,player):
		enemyVec = pygame.math.Vector2(self.rect.center)
		playerVec = pygame.math.Vector2(player.rect.center)
		distance = (playerVec - enemyVec).magnitude()

		if distance > 0:
			direction = (playerVec - enemyVec).normalize()
		else:
			direction = pygame.math.Vector2()

		return (distance,direction)

	def getStatus(self, player):
		distance = self.getPlayerDistanceDirection(player)[0]

		if distance <= self.attackRadius and self.canAttack:
			if self.status != 'attack':
				self.frameIndex = 0
			self.status = 'attack'
		elif distance <= self.noticeRadius:
			self.status = 'move'
		else:
			self.status = 'idle'

	def actions(self,player):
		if self.status == 'attack':
			self.attackTime = pygame.time.get_ticks()
			print('attack')
		elif self.status == 'move':
			self.direction = self.getPlayerDistanceDirection(player)[1]
		else:
			self.direction = pygame.math.Vector2()

	def animate(self):
		animation = self.animations[self.status]
		
		self.frameIndex += self.animationSpeed
		if self.frameIndex >= len(animation):
			if self.status == 'attack':
				self.canAttack = False
			self.frameIndex = 0

		self.image = animation[int(self.frameIndex)]
		self.rect = self.image.get_rect(center = self.hitbox.center)

	def cooldown(self):
		if not self.canAttack:
			currentTime = pygame.time.get_ticks()
			if currentTime - self.attackTime >= self.attackCooldown:
				self.canAttack = True

	def update(self):
		self.move(self.speed)
		self.animate()
		self.cooldown()

	def enemyUpdate(self,player):
		self.getStatus(player)
		self.actions(player)