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
  pass


present_students=[]
student_name=input('請輸入學生姓名:')
while student_name!='q':
  if student_name in present_students:
    print(f'「[{student_name}] 已經點過名囉！」')
  else:
    present_students.append(student_name)
    print(f'「[{student_name}] 簽到成功！」')
  student_name = input('請輸入學生姓名:')

print("今天所有到課的學生名單")
print(f'{present_students}')
