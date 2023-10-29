age_s = input('Please input your age:')
if age_s.isdigit():
  age = int(age_s)
  if age >= 18:
      print("You are an adult.")
  elif age >= 13:
      print("You are a teenager.")
  else:
      print("You are a child.")
else:
  print('Please input an interger for the age')