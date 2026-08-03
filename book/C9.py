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
    print(thing , "is None")
  elif thing:
    print(thing , "is True")
  else:
    print(thing, "is False")

tt=(0,0.0,'',"",'''''',(),[],{},set(),0.00001,[0],[''],' ')
for ts in tt:
  whatis(ts);
