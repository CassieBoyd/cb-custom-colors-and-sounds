from vehicle import Vehicle

class Ecto1(Vehicle):
    def __init__(self, main_color, max_occupancy, powered_by, make, model, special_feature):
        super().__init__(main_color, max_occupancy, powered_by, make, model)
        self.special_feature = special_feature
