

def find_two_mul(a:list[int],b:list[int]) -> int:
  if len(a)!= len(b):
    return -1

  a.sort()
  b.sort()
  sum_value:int=0
  for i in range(0,len(a)):
    sum_value+=(a[i]*b[i])

  return sum_value



print(f'{[1,2,3]} , {[4,5,1]} 最大乘積和為: {find_two_mul([1,2,3],[4,5,1])}')

print(f'{[5,1,3,4,2]} , {[8,10,9,7,6]} 最大乘積和為: {find_two_mul([5,1,3,4,2],[8,10,9,7,6])}')