from vehicle import vehicle

class car(vehicle):

	ac = 0
	steering_wheel= None
	seat_belt = None
	audio_play = None
	no_of_wheels = 0

	def  __init__ (self,ac,steering_wheel,seat_belt,audio_play,no_of_wheels,speed,weight,mileage,color):
		self.ac = ac
		self.steering_wheel = steering_wheel
		self.seat_belt = seat_belt
		self.audio_play = audio_play
		self.no_of_wheels = no_of_wheels
		vehicle.__init__(self,no_of_wheels,speed,weight,mileage,color)

	def deploy_airbags(self):
		print("air bags out")

