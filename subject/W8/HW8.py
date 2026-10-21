def a():
  prize = ['5000元紅包', 'iPad', 'iPhone']

  winner_records = []

  winner_name = input("請輸入中獎員工英文姓名（輸入 q 結束）：")
  while winner_name != "q":
    winner_records.append(f"{winner_name}獲得{prize.pop(-1)}")

    if len(prize) == 0:
      print("獎品已全數抽完！")
      break
    winner_name = input("請輸入中獎員工英文姓名（輸入 q 結束）：")

  sorted_winner_records = sorted(winner_records)

  print(f'{sorted_winner_records}')


'''
班級點名系統
題目需求：
1. 建立一個名為 present_students（已到學生）的空 List。
2. 使用 while 迴圈讓老師不斷輸入學生名字(小寫英文姓名)。
3. 防呆與判斷：
	• 如果名字輸入 q，代表點名結束，跳出迴圈。
	• 如果輸入的名字已經在 present_students 裡面了，請印出：「[名字] 已經點過名囉！」。
	• 如果不在裡面，再使用 append() 把名字加進去，並印出：「[名字] 簽到成功！」。
4. 迴圈結束後，印出今天所有到課的學生名單。
'''


def b():
  present_students = []
  student_name = input('請輸入學生姓名:')
  while student_name != 'q':
    if student_name in present_students:
      print(f'「[{student_name}] 已經點過名囉！」')
    else:
      present_students.append(student_name)
      print(f'「[{student_name}] 簽到成功！」')
    student_name = input('請輸入學生姓名:')

  print("今天所有到課的學生名單")
  print(f'{present_students}')


'''
找出重複的數字
【題目敘述】
請撰寫一個程式，讓使用者輸入一串由空白隔開的整數。程式需要找出這串數字中，
所有出現次數大於或等於 2 次（即有重複）的數字。
【輸入說明】
• 輸入為一行字串，包含多個整數，彼此之間以空白隔開。
【輸出說明】
• 請依據數字在原始輸入中出現的先後順序，印出所有重複出現的數字，數字之間以空白隔開。
• 每個重複的數字只能輸出一次（不可重複列出）。
• 若輸入的數字中完全沒有任何重複的數字，請輸出字串 None。
【範例】
輸入:3 5 2 5 8 3 2 5
輸出:3 5 2
'''


def c():
  number_list = input("請輸入一串文字，並用分隔符開隔開").split()

  number_print_value = []

  for i in number_list:
    if not(i in number_print_value):
      if number_list.count(i) > 1 :
        number_print_value.append(i)

  print(number_print_value)


'''
成績排行榜（排名與分數輸出）
【題目敘述】
學校舉辦了一場考試，請撰寫一個程式來協助老師計算學生的名次。程式會先讀取學生的總人數，接著讀取所有學生的考試分數。請將這些分數由高到低（從大到小）進行排序，並依序輸出每位學生的「名次」與「分數」。
【輸入說明】
• 第一行輸入一個正整數 n，代表學生的總人數（即分數的個數）。
• 第二行輸入 n 個整數，代表每位學生的分數，分數之間以空白隔開。
【輸出說明】
• 請依據分數從大到小排列，輸出 n 行。
• 每行包含兩個數字：第一個數字為名次（從 1 開始），第二個數字為該名次的分數，兩個數字之間以空
  白隔開。
【輸入範例】
  5
  80 95 70 90 85
 【輸出範例】
  1 95
 2 90
 3 85
 4 80
 5 70
'''


def d():
  student_number = int(input("請輸入學生人數"))
  student_score = input(
      "輸入 n 個整數，代表每位學生的分數，分數之間以空白隔開").split()
  if len(student_score) == student_number:
    student_score.sort(reverse=True)

    for i in range(0, student_number):
      print(f'{(i + 1)} : {student_score[i]}')

  else:
    print(
      f"學生人數：{student_number} 與 學生成績數：{len(student_score)} 對不起來，請重新確認")

