s = input("Please input your encrypted message:")
decrypt_s = ""
len_s = len(s)
i = 0
while i < len_s:
  j = i + 1
  while j < len_s and s[j].isdigit():
    j += 1
  decrypt_s += s[i] * int(s[i+1:j])
  i = j

print(decrypt_s)
