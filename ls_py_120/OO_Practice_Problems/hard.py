class WheelsMixin:
    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

class Vehicle:
    def __init__(self,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

    def range(self):
        return self.fuel_capacity * self.fuel_efficiency
    
class LandVehicle(Vehicle):
    pass

class Auto(WheelsMixin, LandVehicle):
    
    def __init__(self, tire_list, 
                 kilometers_per_liter, 
                 liters_of_fuel_capacity):
        super().__init__(kilometers_per_liter, liters_of_fuel_capacity)
        self.tires = tire_list
        
class Motorcycle(WheelsMixin, LandVehicle):
    def __init__(self, tire_list, 
                 kilometers_per_liter, 
                 liters_of_fuel_capacity): 
        super().__init__(kilometers_per_liter, liters_of_fuel_capacity)
        self.tires = tire_list

class WaterVehicle(Vehicle):
    def __init__(self, kilometers_per_liter, 
                 liters_of_fuel_capacity, 
                 number_propellers, 
                 number_hulls):
        super().__init__(kilometers_per_liter, liters_of_fuel_capacity)
        self.number_propellers = number_propellers
        self.number_hulls = number_hulls
    
    def range(self):
        return super().range() + 10

class Catamaran(WaterVehicle):
    pass
        
class Motorboat(WaterVehicle):
    pass
        