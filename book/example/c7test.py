
years_list=[numbersA for numbersA in range(1988,1993)]
print(f'years_list:{years_list}')

print(f'third year:{years_list[3]}')

print(f'oldest year:{years_list[-1]}')

things=['mozzarella','cinderella','salmonella']

for thing in things:
  thing=thing.title()
  print(thing)

print(f'things:{things}')

things[0]=things[0].upper()
print(things[0])