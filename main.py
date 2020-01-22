from bike import Bike
from car import Car

def main():
	bike = Bike()
	car = Car()
	car.start()
	bike.pedal()
	print(car.color)
	print(bike.name)
main()
