class Vehicle():
    def __init__(self, main_color, max_occupancy, powered_by, make, model):
        self.main_color = main_color
        self.max_occupancy = max_occupancy
        self.powered_by = powered_by
        self.make = make
        self.model = model

    def drive(self):
        print("Vrooooom!")

    def turn(self, direction):
        print(f"The {self.model} turned {direction}.")

    def stop(self):
        print(f"The {self.model} stopped.")
