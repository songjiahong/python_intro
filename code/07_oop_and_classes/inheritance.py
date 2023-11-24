class Car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

  def describe_car(self):
    return f"{self.year} {self.make} {self.model}"

class ElectricCar(Car):
  def __init__(self, make, model, year, battery_size=75):
    # Initialize attributes from the parent class
    super().__init__(make, model, year)
    # Add new attribute specific to ElectricCar
    self.battery_size = battery_size

  def describe_battery(self):
    return f"This car has a {self.battery_size}-kWh battery."

  # Overriding the describe_car method from Car
  def describe_car(self):
    description = super().describe_car()
    return f"{description} (Electric)"
