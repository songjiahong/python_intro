message = input("What is your message? ")
encrypt_msg = ''
for char in message:
  encrypt_char = chr(ord(char) + 1)
  encrypt_msg += encrypt_char
print(encrypt_msg)