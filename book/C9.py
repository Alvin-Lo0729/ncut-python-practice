def do_nothing():
  pass


do_nothing()


def make_a_sound():
  print("quack")


make_a_sound()


def agree():
  return False


if agree():
  print("Splendid!")
else:
  print("That was unexpected.")


def echo(anything):
  return anything + " " + anything


print(echo("Rumplestiltskin"))


def commentary(color):
  if color == "red":
    return "It's a tomato."
  elif color == "green":
    return "It's a green pepper."
  elif color == "bee purple":
    return "I don't know what it is, but only bees can see it."
  else:
    return f"I've never heard of the color {color}."


for color in ['red', 'green', 'bee purple', 'shit']:
  print(commentary(color))


def whatis(thing):
  if thing is None:
    print(thing, "is None")
  elif thing:
    print(thing, "is True")
  else:
    print(thing, "is False")


tt = (0, 0.0, '', "", '''''', (), [], {}, set(), 0.00001, [0], [''], ' ')
for ts in tt:
  whatis(ts);


def menu(wine, entree, dessert):
  return {"wine": wine, "entree": entree, "dessert": dessert}


print(f'menu:{menu('chardonnay', 'chicken', 'cake')}')

menu_data = menu(entree="dddd", dessert="eeee", wine="aaa")
print(f'menu:{menu_data}')


def menu2(wine="chardonnay", entree="no way", dessert="pudding"):
  return {"wine": wine, "entree": entree, "dessert": dessert}


print(f'menu2:{menu2(wine="coke")}')


def print_args(*args):
  print(f'Positional tuple:{args}')


print_args(1, 2, 3, 4)
print(f'---------------------')
print_args()


def print_kwargs(**kwargs):
  return kwargs


kw = print_kwargs(wine='abcd', sasdfs='dddd', dessert='pudding')
print(kw.get('wine'))


def print_data(data, *, start=0, end=100):
  for value in (data[start:end]):
    print(value)


data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print_data(data)
print(f'===================')
print_data(data, start=5)

print(f'===================')


def echo(anything):
  'echo returns its input argument'
  return anything;


help(echo)
print(f'==================')
help(echo.__doc__)
print(f'==================')


def answer():
  print(42)


def run_something(func):
  func()


run_something(answer)


def add_args(arg1, arg2):
  print(arg1 + arg2)


# def run_something_with_args(func,arg1,arg2):
#   func(arg1,arg2)
#
# run_something_with_args(add_args(5,9))

def sum_args(*args):
  return sum(args)


def run_with_positional_args(func, *args):
  return func(*args)


sumValue = run_with_positional_args(sum_args, 1, 2, 3, 4)
print(sumValue)


def outer(a, b):
  def inner(c, d):
    return c + d

  return inner(a, b)


print(outer(4, 7))


def knights2(saying):
  def inner2():
    return "we are the knights who say: '%s'" % saying

  return inner2


a = knights2("hello")
print(type(a))
print(a)
b = knights2("world")
print(type(b))
print(b)
print(a())
print(b())


def edit_story(words, func):
  for word in words:
    print(func(word))


stairs = ['thud', 'meow', 'thud', 'hiss']


def enliven(word):
  return word.capitalize() + "!"


edit_story(stairs, enliven)
print("=====================")
edit_story(stairs, lambda word, kk='55': word.capitalize() + "!")

print(sum(range(1, 101)))


def my_range(first=0, last=10, step=1):
  number = first
  while number < last:
    yield number
    number += step


print(my_range())

rangersValue = my_range(1, 5)

for x in rangersValue:
  print(f'hi x:{x}')


def document_it(func):
  def new_function(*args, **kwargs):
    print('Running function:', func.__name__)
    print('Positional arguments:', args)
    print('Keyword arguments:', kwargs)
    result = func(*args, **kwargs)
    print('Result:',result)
    return result
  return new_function

def add_ints(a,b):
  return a+b

add_ints(3,5)

cooler_add_ints= document_it(add_ints)
cooler_add_ints(3,9)

@document_it
def add_ints(a,b):
  return a-b

add_ints(9,8)


def square_it(func):
  def new_function(*args,**kwargs):
    result=func(*args,**kwargs)
    return result*result
  return new_function


print()