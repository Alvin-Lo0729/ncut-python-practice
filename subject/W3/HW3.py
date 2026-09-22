'''
三數找最大值
【題目】請使用者輸入三個不一樣的整數，利用 if-elif-else 結構找出其中的最大值並輸出。

【預期輸出】（輸入 35, 12, 89）：最大值是: 89
'''
print(f'請輸入3個數字，幫你判別哪個最大')
side_a = int(input("請輸入第一個數字"))
side_b = int(input("請輸入第二個數字"))
side_c = int(input("請輸入第三個數字"))
if side_a >= side_b:
  if side_a >= side_c:
    print(f'最大的數字為:{side_a}')
  else:
    print(f'最大的數字為:{side_c}')
elif side_b >= side_c:
  print(f'最大的數字為:{side_b}')
else:
  print(f'最大的數字為:{side_c}')