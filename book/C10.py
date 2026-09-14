# class Car():
#   pass
#
# class Yugo(Car):
#   pass
#
# print(issubclass(Yugo,Car))
#
# give_me_a_car=Car()
# give_me_a_yugo=Yugo()


class Car():
  def exclaim(self):
    print("I'm a Car!")


class Yugo(Car):
  def exclaim(self):
    print("I'm a Yugo")

  def need_a_push(self):
    print("A little help here?")

give_me_a_car=Car()
give_me_a_yugo=Yugo()

give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

class Person():
  def __init__(self,name):
    self.name=name

class MDPerson(Person):
  def __init__(self,name):
    self.name="Doctor "+name

class JDPerson(Person):
  def __init__(self,name):
    self.name=name+", Esquire"

class EmailPerson(Person):
  def __init__(self,name,email):
    super().__init__(name)
    self.email=email

person=Person("Fudd")
doctor=MDPerson("Fudd")
lawyer=JDPerson("Fudd")
me=EmailPerson("Fudd",'ak47237496@gmail.com')

print(f'person name:{person.name}')
print(f'doctor name:{doctor.name}')
print(f'lawyer name:{lawyer.name}')
print(f'me name:{me.name} , my email:{me.email}')

give_me_a_yugo.need_a_push()

class Animal:
  def says(self):
    return "I speak!"

class Horse(Animal):
  def says(self):
    return "Neigh!"

class Donkey(Animal):
  def says(self):
    return "Hee-haw"

class Mule(Donkey,Horse):
  pass

class Hinny(Horse,Donkey):
  pass


print(Mule.mro())
print("========")
print(Hinny.mro())