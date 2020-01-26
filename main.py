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
- Override the drive() method in all the other vehicle classes. Include the vehicle's color in the message (i.e. "The blue Ram drives past. RRrrrrrummbbble!").
- Create a turn(self, direction) method, and a stop(self) method on Vehicle. Define a basic implementation of each.
- Override all three of those methods on some of the vehicles. For example, the stop() method for a plane would be to output the message "The white Cessna rolls to a stop after rolling a mile down the runway."
- Make your vehicle instances perform all three behaviors.
"""

deans_car = Baby("black", 6, "gasoline", "Chevy", "Impala", "Weapons depot in trunk.")

wayne_tech = Batmobile("black", 2, "gasoline", "Chevy", "Impala", "All of them.")

who_you_gonna_call = Ecto1("white", 4, "gasoline", "Futura Duplex", "Cadillac", "Gunner seat, ya'll!")

turtle_power = Party_Wagon("yellow", 8, "gasoline", "Volkswagen", "Bus", "Pizza launcher.")

mustang_sally = Mustang("cherry red", 5, "gasoline", "Ford", "Mustang", 1965)

starman = Tesla("red", 5, "electricity", "Tesla", "Roadster", "It's in friggin' space!")