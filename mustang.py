from vehicle import Vehicle

class Mustang(Vehicle):
    def __init__(self, main_color, max_occupancy, powered_by, make, model, year):
        super().__init__(main_color, max_occupancy, powered_by, make, model)
        self.year = year

    def drive(self):
        print(f"The {self.main_color} {self.year} {self.model} pulls into my driveway. RrrRrruuummmblle!")

    def turn(self, direction):
        print(f"I bust a {direction} and I'm heading to the next block")

    def stop(self):
        print(f"All right stop. Collaborate and listen. Ice is back with my brand new {self.model}")