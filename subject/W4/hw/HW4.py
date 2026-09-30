'''
找出因數並計算因數個數
【問題描述】請撰寫一個 Python 程式，讓使用者輸入一個正整數 n，使用 for 迴圈找出 n 的所有因數，並計算總共有幾個因數。

【預期輸出結果】

   請輸入一個正整數 n：12

   12 的因數有：1, 2, 3, 4, 6, 12

   總共有 6 個因數。
'''

number = int(input("請輸入一個數字，幫你算他的公因數"))
list_value = []

for x in range(1, number + 1):
  if number % x == 0:
    list_value.append(x)

print(f"{number}的因數有:{list_value}，總共有{len(list_value)}個因數")
