class vehicle():

	no_of_wheels = 0
	weight = 0
	speed = 0
	mileage = 0
	color = None

	def __init__(self,no_of_wheels,speed,weight,mileage,color):
		self.no_of_wheels = no_of_wheels
		self.weight = weight
		self.mileage = mileage
		self.color = color

	def go_forwad(self):
		print("moving in front")		

	def reverse(self):
		print("vehicle is moving back")

	def stop(self):
		print("the car has stopped") 
