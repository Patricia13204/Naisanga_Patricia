print("\n--- Method Overriding ---")


class Vehicle:
    def start_engine(self):
        print("Vehicle engine started.")

class Car(Vehicle):
    def start_engine(self):
      print("Car engine is roaring!")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine is rumbling.")


generic_vehicle = Vehicle()
my_car = Car()
my_motorcycle = Motorcycle()

generic_vehicle.start_engine()
my_car.start_engine()
my_motorcycle.start_engine()

