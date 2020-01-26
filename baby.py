from vehicle import Vehicle

class Baby(Vehicle):
    def __init__(self, main_color, max_occupancy, powered_by, make, model, special_feature):
        super().__init__(main_color, max_occupancy, powered_by, make, model)
        self.special_feature = special_feature

    def drive(self):
        print(f"The {self.main_color} {self.model} cruises past. Puuuuuuurrrr...")