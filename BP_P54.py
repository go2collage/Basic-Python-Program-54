# Python Program

# Multiple Inheritance

class Car1():

    # Attributes 
    name = "Jaguar"
    vehicle_type = "Four-wheeler"
    price = 9876034

    # Method
    def show1(self):
        print("Car Name: ", self.name)
        print("Type: ", self.vehicle_type)
        print("Price: ", self.price)

class Car2():
    # Attribute
    name = "BMW 3"
    vehicle_type = "Four-wheeler"
    print = 4569807

    # Method

    def show2(self):
        print("Car Name: ", self.name)
        print("Type: ", self.vehicle_type)
        print("Price: ", self.print)

# Inheritance

class Vehicle(Car1, Car2):
    print("******************* Vehicles *******************")


# Create object
obj = Vehicle()

# Call Method
obj.show1()
obj.show2()

# Thanks for Watching
