# 1
years_list=[numbersA for numbersA in range(1988,1993)]
print(f'years_list:{years_list}')
# 2
print(f'third year:{years_list[3]}')
# 3
print(f'oldest year:{years_list[-1]}')
# 4
things=['mozzarella','cinderella','salmonella']

for thing in things:
  thing=thing.title()
  print(thing)
# 5
print(f'things:{things}')
# 6
things[0]=things[0].upper()
print(things[0])
#7
things.remove(things[2])
print(f'things:{things}')

surprise=['Groucho','Chico','Harpo']

surprise[-1]=surprise[-1].lower();

surprise.reverse()

surprise[0]=surprise[0].title()

print(f'surprise:{surprise}')


even=[numbers for numbers in range(1,10) if numbers % 2==0]
print(f'even:{even}')

