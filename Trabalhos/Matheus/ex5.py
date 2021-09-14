cars = 100
space_in_a_car = 4.0
drivers = 30
passangers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
avarage_passangers_per_car = passangers / cars_driven

print("There are", cars, "cars avaliable.")
print("There are only", drivers, "drivers avaliable.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passangers, "to carpool today.")
print("we need to put about",avarage_passangers_per_car,"in each car")

