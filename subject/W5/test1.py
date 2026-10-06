
sum1=0
for i in range(1,11):
  sum1=sum1+i



for i in range(1,4):
  for j in range(1,4):
    print(f'{i}x{j}={i*j}',end="\t")
  print()


# count=int(input("請輸入要顯示幾階星星"))
#
# for i in range(0,count):
#   for j in range(0,i+1):
#     print("*",end="")
#   print()

# number1=1
# sum1=0
# while number1<=10:
#   sum1=sum1+number1
#   number1=number1+1
#
# print(f'sum1:{sum1}')
#
# for i in range(10):
#   if i==6:
#     break
#   print(i,end="\t")
#
# print("=============")
# for i in range(10):
#   if i==6:
#     continue
#   print(i, end="\t")

account=""
password=""

for i in range(0,3):
  account=input("請輸入帳號：")
  if account!="admin":
    print("帳號錯誤,請重新輸入")
    continue
  else:
    for j in range(0, 3):
      password = input("請輸入密碼：")
      if password != "abcd1234":
        print("密碼錯誤,請重新輸入")
        continue
      else:
        print("密碼正確，歡迎進入本系統")
        break
    break

