from vehicle import vehicle
from car import car
from bike import bike	

class atv(car,bike):
	protective_gear = None

	def __init__(self,protective_gear,ac,steering_wheel,seat_belt,audio_play,no_of_wheels,speed,weight,mileage,color,handle,is_gear):
		self.protective_gear = protective_gear
		car.__init__(self,ac,steering_wheel,seat_belt,audio_play,no_of_wheels,speed,weight,mileage,color)
		bike.__init__(self,handle,is_gear,no_of_wheels,speed,weight,mileage,color)

	def features(self):
		print("protective gear is on")
