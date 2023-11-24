s = input("Please input your message:")
encrypt_s = ""
len_s = len(s)
i = 0
while i < len_s:
  encrypt_s += s[i]
  count = 1
  for j in range(i+1, len_s):
    if s[j] == s[i]:
      count += 1
    else:
      break
  encrypt_s += str(count)
  i += count

print(encrypt_s)
