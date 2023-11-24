class Dog:
  # Constructor method to initialize the dog's attributes
  def __init__(self, name, height, weight):
    self.name = name
    self.height = height
    self.weight = weight
    self._food = None

  @property
  def food(self):
    return self._food
  
  @food.setter
  def food(self, food):
    self._food = food

  # Method to run
  def run(self):
    return print(f"{self.name} is running.")

  # Method to run
  def play(self):
    return print(f"{self.name} is playing.")

  # Method to run
  def eat(self):
    return print(f"{self.name} is eating {self.food}.")

my_dog = Dog('puppy', 60, 30)
my_dog.food = 'meat'

my_dog.eat()