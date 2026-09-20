class Cat:
  def __init__(self, name, age):
    self.name = name
    self.age = age


# a_cat=Cat()
# another_cat=Cat()
#
# print(a_cat)
# print(another_cat)
#
# a_cat.age=3
# a_cat.name="abcd"
# a_cat.namesis=another_cat


# print(a_cat.age)
# print(a_cat.name)
# print(a_cat.namesis)


furball = Cat("furball", 5)
print(furball)
print(furball.age)
print(furball.name)


class Car():
  def exclaim(self):
    print("i am a Car!")


class Yugo(Car):
  def exclaim(self):
    print("i am a Yugo! Much like a Car, but more Yugo-ish")


print(issubclass(Yugo, Car))

give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()


class Person():
  def __init__(self, name):
    self.name = name


class MDPerson(Person):
  def __init__(self, name):
    self.name = "Doctor " + name


class JDPerson(Person):
  def __init__(self, name):
    self.name = name + ", Esquire"


person = Person("Fudd")
docker = MDPerson("Fudd")
lawyer = JDPerson("Fudd")

print(person.name)
print(docker.name)
print(lawyer.name)


class Animal:
  def says(self):
    return "I speak!"


class Horse(Animal):
  def says(self):
    return "Neigh!"


class Donkey(Animal):
  def says(self):
    return "Hee-haw!"


class Mule(Donkey, Horse):
  pass


class Hinny(Horse, Donkey):
  pass


print(Mule.mro())
print(Hinny.mro())

mule = Mule()
hinny = Hinny()

print(mule.says())
print(hinny.says())


class PrettyMixin():
  def dump(self):
    import pprint
    pprint.pprint(vars(self))


class Thing(PrettyMixin):
  pass


t = Thing()
t.name = "Nyarlathotep"
t.feature = "ichor"
t.age = "eldritch"

print(t.dump())


class Duck():
  def __init__(self, input_name):
    self.__name = input_name

  @property
  def name(self):
    print('inside the getter')
    return self.__name

  @name.setter
  def name(self, input_name):
    print("inside the  setter")
    self.__name = input_name


class Circle():
  def __init__(self,radius):
    self.radius = radius

  @property
  def  diameter(self):
    return 2  * self.radius

c=Circle(5)
print(c.radius)
print(c.diameter)

c.radius = 10
print(c.radius)
print(c.diameter)

fowl=Duck("Howard")
print(fowl.name)
fowl.name="Donald"
print(fowl.name)


class Fruit:
  color = "red"


blueberry=Fruit()
print(Fruit.color)
print(blueberry.color)

blueberry.color = "blue"
print(Fruit.color)
print(blueberry.color)

Fruit.color="orange"
print(Fruit.color)
print(blueberry.color)

new_fruit=Fruit()
print(new_fruit.color)


class A():
  count = 0
  def __init__(self):
    A.count += 1

  def exclaim(self):
    print("I'm an A")

  @classmethod
  def kids(cls):
    print("A has" ,  cls.count," little objects.")


easy_a=A();
breezy_a=A();
wheezy_a=A();
print(A.kids())


class CoyoteWeapon():
  @staticmethod
  def commercial():
    print("This CoyoteWeapon has been brought to you by Acme")


CoyoteWeapon.commercial()

class Quote():
  def __init__(self,person,words):
    self.person = person
    self.words = words

  def who(self):
    return self.person

  def says(self):
    return self.words+"."

class QuestionQuote(Quote):
  def says(self):
    return self.words+"?"

class  ExclamationQuote(Quote):
  def says(self):
    return self.words+"!"

hunter=Quote("Elmer Fudd","I'm hunting wabbits")
print(hunter.who(),"  says:",hunter.says())

hunted1=QuestionQuote("Bugs Bunny","what's up,doc")
print(hunted1.who(),"  says:",hunted1.says())

hunted2=ExclamationQuote("Daffy Duck","It's rabbit season")
print(hunted2.who(),"  says:",hunted2.says())
