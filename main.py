from vehicle import Vehicle
from baby import Baby
from batmobile import Batmobile
from ecto1 import Ecto1
from party_wagon import Party_Wagon
from mustang import Mustang
from tesla import Tesla

"""
X- Define 5 of your favorite vehicles
X- Move all common properties in your vehicles to a new Vehicle class.
X- Create an instance of each vehicle.
X- Define a different value for each vehicle's properties.
X- Create a drive() method in the Vehicle class.
X- Override the drive() method in all the other vehicle classes. Include the vehicle's color in the message (i.e. "The blue Ram drives past. RRrrrrrummbbble!").
X- Create a turn(self, direction) method, and a stop(self) method on Vehicle. Define a basic implementation of each.
- Override all three of those methods on some of the vehicles. For example, the stop() method for a plane would be to output the message "The white Cessna rolls to a stop after rolling a mile down the runway."
- Make your vehicle instances perform all three behaviors.
"""

deans_car = Baby("black", 6, "gasoline", "Chevy", "Impala", "Weapons depot in trunk.")

wayne_tech = Batmobile("black", 2, "gasoline", "Chevy", "Batmobile", "All of them.")

who_you_gonna_call = Ecto1("white", 4, "gasoline", "Futura Duplex", "Cadillac", "Gunner seat, y'all!")

turtle_power = Party_Wagon("yellow", 8, "gasoline", "Volkswagen", "Bus", "Pizza launcher.")

mustang_sally = Mustang("cherry red", 5, "gasoline", "Ford", "Mustang", 1965)

starman = Tesla("red", 5, "electricity", "Tesla", "Roadster", "It's in friggin' space!")

# for key, value in deans_car.__dict__.items():
#     print(f'{key}: {value}\n')

# deans_car.drive()
# deans_car.turn("left")
# deans_car.stop()

# for key, value in wayne_tech.__dict__.items():
#     print(f'{key}: {value}\n')

# wayne_tech.drive()
# wayne_tech.turn("right")
# wayne_tech.stop()

# for key, value in who_you_gonna_call.__dict__.items():
#     print(f'{key}: {value}\n')

# who_you_gonna_call.drive()
# who_you_gonna_call.turn("left")
# who_you_gonna_call.stop()

# for key, value in turtle_power.__dict__.items():
#     print(f'{key}: {value}\n')

# turtle_power.drive()
# turtle_power.turn("left")
# turtle_power.stop()

for key, value in mustang_sally.__dict__.items():
    print(f'{key}: {value}\n')

mustang_sally.drive()
mustang_sally.turn("right")
mustang_sally.stop()

# for key, value in starman.__dict__.items():
#     print(f'{key}: {value}\n')

# starman.drive()
# starman.turn("right")
# starman.stop()