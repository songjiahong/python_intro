s = input("How old are you?")
if s.isdigit():
  age = int(s) + 3
  print(f"Your age is {age} after 3 years")
else:
  print(f"{s} is not an integer. Please input an integer number!")