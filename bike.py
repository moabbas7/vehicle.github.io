from vehicle import vehicle

class bike(vehicle):

	handle = 0
	is_gear = 0

	def __init__(self,handle,is_gear,no_of_wheels,speed,weight,mileage,color):
		self.handle = handle
		self.is_gear = is_gear
		vehicle.__init__(self,no_of_wheels,speed,weight,mileage,color)

	def wheelie(self):
		print("the bike doing a wheelie")

	def stopping(self):
		print("the bike has stopped")
	
