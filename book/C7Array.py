import copy
from os.path import split

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

work_quotes=['Working hard?','Quick question!','Number one priorities']
print(work_quotes)

work_quotes.clear()
print(work_quotes)

marxes=['Groucho', 'Chico', 'Harpo','Zeppo']
print(marxes.index('Chico'))

simpsons=['Lisa','Bart','Marge','Homer','Bart']
print(simpsons.index('Bart'))


print('Bbb' in simpsons)
print("Lisa" in simpsons)

marxes=['Groucho','Choico','Harpo','Choico']
print(marxes.count('Choico'))

print(" | ".join(marxes))

friends=['Harry','Hermione','Ron']
separator=' * '
joined=separator.join(friends)
print(joined)

separated=joined.split(separator)
print(separated)
print(separated.__eq__(friends))


marxes=['Groucho','Chico','Harpo']
sorted_marxes=sorted(marxes)
print("sorted_marxes:",sorted_marxes)
print("marxes:",marxes)

marxes.sort()
print(f"marxes:{marxes}")

numbers=[2,1,4.0,3]
numbers.sort()
print(numbers)
numbers=[2,1,4.0,3]
numbers.sort(reverse=True)
print(numbers)


marxes=['Groucho','Chico','Harpo']
print(len(marxes))

print('============')

a=[1,2,3]
print(f'a:{a}')
b=a
print(f'b:{b}')
a[0]='surprise'
print(f"a:{a}")
print(f'b:{b}')

print("=========")

a=[1,2,3]
b=a.copy();
c=list(a)
d=a[:]

a[0]='aaaaaa'

print(f'a:{a}')
print(f'b:{b}')
print(f'c:{c}')
print(f'd:{d}')

print("=========")

a=[1,2,[8,9]]

b=copy.deepcopy(a);
print(f'a:{a}')
print(f'b:{b}')

a[2][1]=10;
print(f'a:{a}')
print(f'b:{b}')

a=[7,2]
b=[7,2,9]

print(f'a==b:{a==b}')
print(f'a<=b:{a<=b}')
print(f'a<b:{a<b}')
# page113

cheeses=['brie','gjetost','havarti']
for cheese in cheeses:
  print(f'cheese:{cheese}')

