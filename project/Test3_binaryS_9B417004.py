

def binary_search(list_value,value):
  left=0
  right=len(list_value)-1
  index=-1
  while left<=right:
    mid=(left+right)//2
    if (list_v := list_value[mid]) == value:
      index=mid
      break
    elif list_v>value:
      right=mid-1
    else:
      left=mid+1
  return index

vv=[1,3,5,7,9]

print(binary_search(vv,1))
print(binary_search(vv,3))
print(binary_search(vv,5))
print(binary_search(vv,7))
print(binary_search(vv,9))
print(binary_search(vv,2))