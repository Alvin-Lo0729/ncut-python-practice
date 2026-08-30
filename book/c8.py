empty_dict = {}

print(empty_dict)
bierce = {
  "day": "A period of teadasf",
  "positive": "sadfasdf",
  "misfortune": "sadfasdfasd"
}

print(f'bierce:{bierce}')

acme_customer = dict(first="wile", middle="E", last="Coyote")
print(f'acme_customer:{acme_customer}')

pythons = {
  "Chapman": "Graham",
  "Cleese": "John",
  "Idle": "Eruc"
}
print(f'pythons:{pythons}')
pythons['Gilliam']='Gerry'
print(f'pythons:{pythons}')

pythons['Gilliam']='Terry'
print(f'pythons:{pythons}')
some_name = {
  "Chapman": "Graham",
  "Cleese": "John",
  "Idle": "Eruc",
  "Cleese": "TTS",
}
print(f'some_name:{some_name}')

if "Idle" in some_name:
  print(f'some_name_Idle:{some_name["Idle"]}')


print(f'some_name_Iddd:{some_name.get("Iddd","is not have this")}')

print(f'some_name_keys:{some_name.keys()}')