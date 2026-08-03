

data = int(input())
st = ""

print(f'{bin(data)}')

if data == 0:
  print(0)
else:
  isUp=data>0
  data=abs(data);
  while data != 1:
    st=str(data%2)+st
    data = int(data / 2)
  print(f'{"" if isUp else "-"}{"1"+st}')
