empty_tuple=()
print(empty_tuple)

one_marx='Groucho',
print(one_marx)
print("type ",type(one_marx))

one_marx2=('Groucho',)
print(one_marx2)
print("type ",type(one_marx2))

marx_tuple='Groucho','Chico','Harpo',
print(marx_tuple)
print("type ",type(marx_tuple))

marx_list=('Groucho','Chico','Harpo')
print(tuple(marx_list))

print(('yoda',)*3)

words=('fresh','out','of','ideas')
for words in words:
  print(words)

t1=('Fee','Fie','For')
t2=('Flop',)
print(t1+t2)

print(id(t1))
print(t1)
t1+=t2

print(id(t1))
print(t1)



