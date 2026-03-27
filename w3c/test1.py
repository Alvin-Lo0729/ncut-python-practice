print("Hello World", end="111")
print("")

x = 4
x = "Sally"

print(x)

x = str(3)
print(type(x))
print(isinstance(x, str))
print("x:", x)
y = int(3);
print(isinstance(y, str))
print("y:", y)
z = float(3)
print("z:", z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = fruits[2]
print(x)
x = y = z = 'Hello World'

x = 333


def myfunc():
    x = 999
    print("Hello World:", x)


myfunc()

print("Hello World:", x)

x = "awesome"


def myFunc2():
    global x
    x = "fantastic"

myFunc2()
print("Python is :", x)


def myfunc3():
    global j
    j="test33333"

myfunc3()
print("python is "+j)