
x=20.5
print(type(x))
x=1j
print(type(x))
x=["apple","banana","cherry"]
print(type(x))
x=("apple","banana","cherry")
print(type(x))
x=range(6)
print(type(x))
x={"name" : "John", "age" : 36}
print(type(x))
print(x)
print(type(x.get("age")))
x = {"apple", "banana", "cherry"}
print(type(x))
x.add("ggg")
print(x)
x = frozenset({"apple", "banana", "cherry"})
print(type(x))
x = b"Hello"
print(x)
x = memoryview(bytes(5))
print(x)
x = None
print(x)

x = complex(33)
print(type(x))
print(x)

x = bytes(5)
print(type(x))
print(x)
x = bytes(3)
print(type(x))
print(x)