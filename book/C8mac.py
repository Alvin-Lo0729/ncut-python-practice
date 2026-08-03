from book.c4 import letter

signals = {'green': 'go', "yellow": "go faster", "red": "stop"}

print(f'signals:{signals}')

print(f'signals keys:{signals.keys()}')
print(f'signals values:{signals.values()}')
print(f'signals items:{signals.items}')
print(f'signals length:{len(signals)}')

first = {'a': "aa", 'b': 'bb'}
second = {'b': "bbc", 'c': 'cc'}
third = {'d': 'ddd'}
unicore = {**first, **second}
print(f'unicore:{unicore}')
unicore = {**first, **second, **third}
print(f'unicore:{unicore}')

py = {
  'chapman': "graham",
  'a': 'apple',
  'c': 'claim',
  'd': 'dog'
}

animal = {
  'ca': 'cat',
  'ti': "tiger"
}

print(f'py:{py}')
py.update(animal)
print(f'py:{py}')
del py['ca']

print(f'py:{py}')
py.update({'ca': 'cats'})

print(f'py.pop:{py.pop('cat', 'no cat')}')

# py.clear()
# print(f'py:{py}')

print(f'ca in py:{'ca' in py}')

for keys in py.keys():
  print(f'{keys} in py:{keys in py}')
  print(f'{keys} value: {py.get(keys, "no this data")}')

# for kk in py:
#   print(f'{kk}:{py.get(kk)}')
print('====================')
for key, value in py.items():
  print(f'{key} to {value}')

word = 'letters'

letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

s = set((1, 2, 3, 4, 5, 1))

print(f's:{s}')
s.remove(2)
print(f's:{s}')

drinks = {
  'martini': {'vodka', 'vermouth'},
  'black russian': {'vodka', 'kahlua'},
  'white russian': {'cream', 'kahlua', 'vodka'},
  'manhattan': {'rye', 'vermouth', 'bitters'},
  'screwdriver': {'orange juice', 'vodka'},
}

# for name,contents in drinks.items():
#   if 'vodka' in contents:
#     print(name)
# for name,contents in drinks.items():
#   if 'vodka' in contents and not('vermouth' in contents or 'cream'in contents):
#     print(name)

for name,contents in drinks.items():
  if contents &{'vermouth','orange juice'}:
    print(name)
