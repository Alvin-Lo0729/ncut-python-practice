'''
(一)數字統計系統
題目說明
請撰寫一個 Python 程式，讓使用者連續輸入整數，直到輸入 -1 時結束輸入。
程式必須利用 while 迴圈，統計所有輸入數字中的最大值、最小值及平均值，並依照指定格式輸出結果。
注意事項：
輸入的整數範圍為 0～1000。
當輸入 -1 時，代表結束輸入，-1 不列入統計。
保證至少會輸入一個有效整數。
平均值必須顯示至小數點後兩位。
程式撰寫限制
1.必須使用 while 迴圈處理連續輸入的整數。
2.必須使用 if 判斷式比較最大值與最小值。
3.不得使用 for 迴圈。
4.不得使用 max()、min()、sum() 等內建函式。
5.不得使用串列（List）儲存所有輸入數字。
輸入範例
80
65
90
75
100
-1
輸出範例
最大值：100
最小值：65
平均值：82.00

'''

input_value = int(input("請輸入數字:"))

while not (0 <= input_value <= 1000):
  print(f'請確認輸入的數字為0~1000')
  input_value = int(input("請重新輸入"))

max_value = input_value
min_value = input_value
sum_value = input_value
count_number = 1

while input_value > -1:
  if 0 <= input_value <= 1000:
    if input_value > max_value:
      max_value = input_value

    if input_value < min_value:
      min_value = input_value

    sum_value += input_value
    count_number = count_number + 1

  input_value = int(input("請輸入數字:"))

print(f'最大值：{max_value}', f'最小值：{min_value}',f'平均值：{(sum_value / count_number):.2f}',sep="\n")
