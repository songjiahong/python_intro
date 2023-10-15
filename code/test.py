message = input("Give me your message:")

result = ''
for char in message:
  interger = ord(char) + 1
  result += chr(interger)

print(result)
