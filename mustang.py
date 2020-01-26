from vehicle import Vehicle

class Mustang(Vehicle):
    def __init__(self, main_color, max_occupancy, powered_by, make, model, year):
        super().__init__(main_color, max_occupancy, powered_by, make, model)
        self.year = year

    def drive(self):
        print("RrrRrruuummmblle!")