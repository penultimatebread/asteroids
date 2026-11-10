import pygame
import circleshape
from logger import log_event
import random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(circleshape.CircleShape):
	def __init__(self, x: float, y: float, radius: float) -> None:
		super().__init__(x, y, radius)

	def draw(self, screen: pygame.surface) -> None:
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

	def update(self, dt: float) -> None:
		self.position += self.velocity * dt

	def split(self) -> None:
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		log_event("asteroid_split")
		angle = random.uniform(20,50)
		velocity1 = self.velocity.rotate(angle)
		velocity2 = self.velocity.rotate(angle * -1)
		velocity2 *= -1
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
		new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
		new_asteroid1.velocity = velocity1 * 1.2
		new_asteroid2.velocity = velocity2 * 1.2
