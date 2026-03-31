emtpy_list = []

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_bird = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
leapYear = [2000, 2004, 2008]
randomness = ['Punxsatawney', {"groundhog"}, 'Phil', "Feb.2"]

another_empty_list = list();
print(another_empty_list)

print(list('cat'))

a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))

take_like_a_pirate_day = '2026/01/01';
print(take_like_a_pirate_day.split("/"))

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])
print(marxes[1])
print(marxes[2])
print("-------")
print(marxes[-1])
print(marxes[-2])
print(marxes[-3])

print(marxes[0:2])

print(marxes[::2])
print(marxes[::-2])
print(marxes[::-1])
marxes.reverse()
print(marxes)

marxes.reverse();

marxes.append('Zeppo')
print(marxes)

print(marxes[::-1])

marxes.remove('Zeppo')
print(marxes)

marxes.insert(2, 'Gummo')
print(marxes)

marxes.insert(10, 'Zeppo')
print(marxes)

print(['bbb']*3)
print('aaa '*3)

others=['GGGGG','BBBB']
marxes.extend(others)

print(marxes)

kkw=['dddd','bbb']
marxes.append(kkw)
print(marxes)
marxes.remove(kkw)
print(marxes)


numbers=[1,2,3,4,5]
numbers[1:3]=[2,0,9]
print(numbers)

marxes = ['Groucho', 'Chico', 'Harpo','Gummo','Karl']

del marxes[-1]
print(marxes)

marxes=['Groucho', 'Chico', 'Harpo','Zeppo']
popValue =marxes.pop()
print(popValue)

print(marxes)

popValue=marxes.pop(1)
print(popValue)
print(marxes)