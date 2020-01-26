from vehicle import Vehicle

class Tesla(Vehicle):
    def __init__(self, main_color, max_occupancy, powered_by, make, model, special_feature):
        super().__init__(main_color, max_occupancy, powered_by, make, model)
        self.special_feature = special_feature

    def drive(self, main_color, model):
        print(f"The {main_color} {model} zips past. Ssssshhhhhh!")
