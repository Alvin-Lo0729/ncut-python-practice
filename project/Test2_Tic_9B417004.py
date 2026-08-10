import random


# 確認是否獲勝
def check_win(board, type_value):
  win_lines = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    # 三橫列
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    # 三直行
    (0, 4, 8), (2, 4, 6),
    # 兩對角線
  ]
  return any(
      board[a] == board[b] == board[c] == type_value
      for a, b, c in win_lines
  )

# 清除棋盤
def clear_board(board):
  for i in range(9):
    board[i] = None

# 放資料
def put(board, position, type_value):
  board[position] = type_value

# 選擇圖形
def choice_input_type():
  while True:
    try:
      print_type = int(input("請選擇你要O還是X, O請選擇1 X選擇2："))
      if print_type==1 or print_type==2:
        return print_type
      else:
        print("請輸入1或2")
    except ValueError:
      print("Error: That input is not an integer.")
# 列印畫面
def print_board(board):
  for i in range(9):
    if board[i] is None:
      print(" ", end="")
    else:
      print(board[i], end="")
    if i % 3 == 2:
      print()
    else:
      print("|", end="")
# 選擇先手
def choice_first():
  while True:
    humane_number = random.randint(0, 10)
    computer_number = random.randint(0, 10)
    if humane_number == computer_number:
      continue
    else:
      return "you" if humane_number > computer_number else "computer"

print("Hello  請開始玩井字遊戲")

board = [None] * 9
print_type=choice_input_type()
user_print_type = "O" if print_type==1 else "X"
computer_print_type = "X" if print_type==1 else "O"
vv={"you":user_print_type,"computer":computer_print_type}

print(f'你的選擇{user_print_type}, 機器人選擇{computer_print_type}')

index_charest=choice_first()

for count in range(9):
  print(f'{index_charest}是{vv.get(index_charest)} ，開始選擇(1~9)')
  if(index_charest=="you"):



