def square(a):
  return a * a

class Car:
  def __init__(self, model, year):
    self.model = model
    self.year = year

  def start_engine(self):
    print(f'Car {self.model} engine starts')