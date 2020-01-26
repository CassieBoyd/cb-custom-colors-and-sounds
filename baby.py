from vehicle import Vehicle

class Baby(Vehicle):
    def __init__(self, main_color, max_occupancy, powered_by, make, model, special_feature):
        super().__init__(main_color, max_occupancy, powered_by, make, model)
        self.special_feature = special_feature

    def drive(self):
        print(f"The {self.main_color} {self.model} cruises past. Puuuuuuurrrr...")

    def turn(self, direction):
        print(f"The {self.model} turned the {direction} corner.")

    def stop(self):
        print(f"The {self.main_color} {self.model} screeched to a halt and Sam and Dean clambered out, weapons raised.")