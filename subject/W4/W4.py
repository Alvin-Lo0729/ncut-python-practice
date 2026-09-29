sum = 0
for x in range(1, 11):
  sum += x

print(f'sum:{sum}')

number = [12, 7, 24, 15, 8, 3]

ans2 = 0;
for x in (x for x in number if x %2==0) :
    ans2 += x

print(f'ans2:{ans2}')
