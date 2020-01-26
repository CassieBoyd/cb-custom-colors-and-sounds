from vehicle import Vehicle

class Mustang(Vehicle):
    def __init__(self, main_color, max_occupancy, powered_by, make, model):
        super().__init__(main_color, max_occupancy, powered_by, make, model)
