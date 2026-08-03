# 8.1

import math

e2f = {
  "dog": 'chien',
  "cat": 'chat',
  "walrus": 'morse',
}

# 8.2
print(e2f.get('walrus', 'no this words'))

# 8.3
f2e = {e2f.get(kk): kk for kk in e2f}
print(f2e)

# 8.4
print(f2e.get('chien', 'no this words'))

# 8.5
print(f'set e2f:{set(e2f)}')

# 8.6
life = {
  'animals': {
    'cats': ['Henri', 'Grumpy', 'Lucy'],
    'octopi': [],
    'emus': []
  },
  'plants': {},
  'other': {}
}

# 8.7
print(life.keys())

# 8.8
print(life['animals'])

# 8.9
print(life['animals']['cats'])

# 8.10
squares = {dd: math.pow(dd, 2) for dd in range(10)}
print(squares)

#8.11
oddValue={kk for kk in range(10) if kk%2==1}
print(oddValue)

#8.12
for thing in (f'Got {number}' for number in range(10)):
  print(thing)

#8.13
key=('optimist','pessimist','troll')
value=('The glass is half full','The glass is half empty','how did you get a glass')

data=dict(zip(key,value))
print(data)

#8.14

titles=['Creature of Habit','Crewel Fate','Sharks on a Plane']
plots=['A nun turns into a monster','A haunted yarn shop','Check your exits']

movie=dict(zip(titles,plots))
print(movie)
print(movie.get('Creature of Habit'))