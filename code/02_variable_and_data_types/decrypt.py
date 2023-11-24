message = input("What is your encrypted message? ")
decrypt_msg = ''
for char in message:
  decrypt_char = chr(ord(char) - 1)
  decrypt_msg += decrypt_char
print(decrypt_msg)