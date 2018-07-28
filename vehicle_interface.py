from car import car
from truck import truck


obj= car("ac","steering_wheel","seat_belt","audio_play")
print(obj.deploy_airbags())

obj1 = truck(100,60,6,40,1500,10,"blue")
print(obj1.load())
print(obj1.unload())
print(obj1.no_of_wheels)
print(obj1.speed)
print(obj1.weight)
print(obj1.mileage)
print(obj1.color)
