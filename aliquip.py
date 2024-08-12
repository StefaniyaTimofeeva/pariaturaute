class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Color: {self.color}, Mileage: {self.mileage}")

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry", 2020, "Red")

# Driving the car
my_car.drive(100)

# Displaying car information
my_car.display_info()
