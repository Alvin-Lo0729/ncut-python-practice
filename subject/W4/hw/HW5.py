'''
最大公因數
問題描述】請撰寫一個 Python 程式，讓使用者輸入兩個正整數 ，使用 for 迴圈找出兩數的最大公因數。

【預期輸出結果】

   請輸入一個正整數 a：12

   請輸入一個正整數 b：18

   最大公因數:6

'''
print("幫你算最大公因數")
number = int(input("請輸入第一個數字"))
number2 = int(input("請輸入第二個數字"))
max_divisors = 1
minNumber=min(number, number2)
for x in range(1, minNumber + 1):
  if number % x == 0 and number2 % x == 0:
    max_divisors = x

print(f"{number} 、 {number2}最大公因數為：{max_divisors}")
