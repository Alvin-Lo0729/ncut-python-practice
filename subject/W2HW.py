'''
請宣告三個變數，分別存放您的名字（字串）、年齡（整數）和居住縣市（字串）。
接著分別使用 f-string / % 標記法語法，
印出像這樣的句子：「您好，我是小明，今年 25 歲，住在台中市。」
'''


name = "羅星傑"
age = 38
city = "南投縣"

print(f"您好，我是{name}，今年{age}歲，住在{city}")
'''
圓形面積（f-string 限制小數點）
變數:半徑=5,pi=3.14159,請計算圓形面積,並使用 f-string 輸出到小數點後 2 位
value=33.2031284
print(f"{value:.3f}") ==>顯示為33.203 （小數點後3位）

計算方式
a=6
b=4
print(a+b) 相加
==>10
print(a-b) 相減
==>2
print(a*b) 相乘
==>24
print(a/b) 求商（有可能會有小數點）
==>1.5
print(a//b) 求商數
==>1
print(a%b) 求餘數
==>2
print(a**b) 次方公式

'''
# 半徑
val=5
#pi
pi=3.14159

#圓面積 pi*r*r==>pir^2

result=pi*val*val

result=pi*(val**2)

print(f'圓面積為：{result:.2f}')

'''
個人資料(print/換行)
請宣告三個變數,要求只能使用一個 print()，輸出範例：
===== 個人資料 =====
姓名：小明
年齡：18
科系：資訊工程系
====================


print("a","b","c","d","e",sep="\n")  (注意沒有加f,\n為換行符號)
會變成
a
b
c
d
e

'''

print(
    "===== 個人資料 =====",
    "姓名：小明",
    "年齡：18",
    "科系：資訊工程系",
    "====================",
    sep="\n",
)
'''
日期格式
請宣告3個變數分別是年月日,請使用sep,輸出範例:

1.設定變數（年、月、日）
2.使用print 函數的sep做中間的介接
如：
print("a","b","c","d","e","f",sep="@")
a@b@c@d@e@f

'''

year = 2026
month = 9
day = 11

print(year, month, day, sep="/")


'''
收據欄位對齊（f-string 靠左與靠右）
請宣告兩個變數：title = "總金額"、amount = 2500。

請利用 f-string 的對齊語法，
讓 title 靠左對齊（總寬度 10），amount 靠右對齊（總寬度 6），
中間不用加任何符號。

1.宣告變數
2.使用print的f-string方法
title = "總金額"
print(f'{title:20}') 為整個印出內容會佔20個空格，title的內容則預設為靠左開始顯示
print(f'{title:>20}') 為整個印出內容會佔20個空格，title的內容則預設為靠右開始顯示
print(f'{title:<20}') 為整個印出內容會佔20個空格，title的內容則預設為靠右開始顯示
print(f'{title:^20}') 為整個印出內容會佔20個空格，title的內容則預設為置中開始顯示
print(f'{title\t} 為印出title的內容後，印出ＴＡＢ控一大格的內容
'''

title = "總金額"
amount = 2500

print(f"{title:<10}")
print(f"{amount:>6}")
