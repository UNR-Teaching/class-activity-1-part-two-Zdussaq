from engine import engine
from wheels import wheels
from vehicle import Vehicle

class Car(Vehicle):
	def __init__(self):
		print("Creating new Car!")
		self.color = "Black"
		self.name = "Honda"
	def start(self):
		print("Your engine fails")
	def drive(self):
		print("Your engine is not on")
	engine = engine("Good")
	wheels = wheels(4)
