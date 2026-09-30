"""
  數字範圍累加
  請撰寫一個 Python 程式，
  讓使用者可以從鍵盤輸入任意一個正整數N。
  程式必須利用 For 迴圈，
  自動計算從1到N之間（包含 N）
  所有「偶數」的相加總和，
  並在螢幕上輸出最終的加總結果。
  """

number = int(input("請輸入一個數字，自動計算從1到N之間（包含 N）所有「偶數」的相加總和"))
if number <= 1:
  print(f'countNumber:{number}')

counter_num = 0
for x in (x1 for x1 in range(1, number + 1) if x1 % 2 == 0):
  counter_num += x
print(f'countNumber:{counter_num}')

