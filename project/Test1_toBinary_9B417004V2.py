

data = input()
try:
  data=int(data)
  print(f'{bin(data)}')
except ValueError:
  print("ValueError")