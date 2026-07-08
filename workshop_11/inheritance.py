class Vehicle:
    def __init__(self, wheels = 0):
        self.wheels = wheels

    def start_engine(self):
        raise NotImplementedError()

    def stop_engine(self):
        raise NotImplementedError()

    def brake(self):
        raise NotImplementedError()


class DieselCar(Vehicle):
    def __init__(self, a, wheels=0):
        super().__init__(wheels)
        self.a = a

    def start_engine(self):
        print("Wroom Wroom")
        print("Starting Engine")

    def stop_engine(self):
        print("Stopping Engine")


class FuelCar(Vehicle):
    pass

class ElectricCar(Vehicle):
    pass

class Bike:
    def start_engine(self):
        pass

class Chopper:
    pass

class Truck:
    pass



vehicles: list[Vehicle] = [DieselCar(7, 4), DieselCar(7, 6), DieselCar(7, 4), DieselCar(7, 6)]

for vehicle in vehicles:
    print(vehicle.wheels)
    vehicle.start_engine()
    vehicle.stop_engine()