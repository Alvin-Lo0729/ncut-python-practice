'''
學生各科成績總分計算
 一、題目說明
某班級需要統計學生的考試成績。由於班級中的學生人數與考試科目數量可能不同，因此希望設計一套簡易的成績統計程式。
請撰寫一個 Python 程式，讓使用者先輸入學生人數 N 與考試科目數量 M，接著依序輸入每位學生的各科成績。
程式必須使用二維 List儲存所有學生的成績，其中每一列代表一位學生，每一欄代表一個科目的成績。
所有成績輸入完成後，請使用巢狀 for 迴圈，依序計算每位學生的成績總分，並輸出結果。

 二、輸入說明
1. 第一行輸入一個正整數 N，代表學生人數。
2. 第二行輸入一個正整數 M，代表每位學生的考試科目數量。
3. 接下來共輸入 N × M 行，每行包含一個整數，代表一科成績。
4. 成績依照學生順序輸入，每位學生依序輸入 M 科成績，完成後再輸入下一位學生的成績。

三、輸入限制
1 ≤ N ≤ 50
1 ≤ M ≤ 10
每科成績為 0～100 的整數
每位學生的科目數量皆相同
'''
from idlelib.query import Goto


def b():
  student_numer = int(input("請輸入學生人數"))
  student_subject_number = int(input("請輸入學生考試科目數量"))

  scores = []
  for i in range(0, student_numer):
    score_row = []
    for j in range(0, student_subject_number):
      sc = int(input(f"請輸入第{i + 1}個學生的，第{j + 1}科成績："))
      score_row.append(sc)
    scores.append(score_row)

  max_score = 0
  max_number = 0
  for i in range(0, len(scores)):
    person_all_score = 0
    for j in scores[i]:
      person_all_score += j
    print(f"第{i + 1}個學生的總成績為：{person_all_score}")
    if person_all_score > max_score:
      max_score = person_all_score
      max_number = (i + 1)

  print(f"總成績最高的同學為:{max_number}號同學，成績為：{max_score}")


'''
矩陣轉置
題目敘述：
請撰寫一個 Python 程式，輸入一個 N×M 的整數矩陣，並將矩陣進行轉置（Transpose）。
矩陣轉置是指將原本矩陣的列與欄互相交換。例如原本是 2 列 3 欄的矩陣，轉置後會變成 3 列 2 欄。
輸入說明： 第一行輸入 N，第二行輸入 M，接下來輸入 N×M 個整數，每個整數獨立一行。
輸出說明： 輸出轉置後的矩陣，每列數字以空格分隔。
'''


def c():
  row_number = int(input("請輸入矩陣列數"))
  column_number = int(input("請輸入矩陣行數"))

  double_list = []
  for i in range(0, row_number):
    row_list = []
    for j in range(0, column_number):
      nu = int(input(f"請輸入矩陣第[{i}][{j}]個元素數字:"))
      row_list.append(nu)
    double_list.append(row_list)

  print("原始矩陣:")
  for i in double_list:
    print(i)

  print("轉換後的矩陣")

  reverse_list = []
  for i in range(0, column_number):
    row_list = []
    for j in range(0, row_number):
      row_list.append(double_list[j][i])
    reverse_list.append(row_list)

  for i in reverse_list:
    print(i)


'''
判斷對稱矩陣
題目說明
在數學中，矩陣是一種由數字依照列（Row）與欄（Column）排列而成的資料結構。
若一個 N×N 的正方形矩陣，以主對角線（左上角至右下角）為對稱軸，主對角線兩側對應位置的元素皆相同，則稱為「對稱矩陣」（Symmetric Matrix）。
換句話說，對於矩陣中任意位置 (i, j)，若皆符合以下條件：
a[i][j] == a[j][i]
則此矩陣為對稱矩陣。
請撰寫一個 Python 程式，讓使用者輸入一個 N×N 的整數矩陣，並使用二維 List儲存矩陣中的所有元素。
接著透過巢狀 for 迴圈與 if 判斷式，檢查此矩陣是否為對稱矩陣。
矩陣符合對稱條件，輸出 YES；否則輸出 NO。
輸入說明
第一行輸入一個正整數 N，代表矩陣的列數與欄數。
接下來共輸入 N×N 行，每行包含一個整數，代表矩陣中的一個元素。
所有元素依照由左至右、由上至下的順序輸入。
輸出說明
輸出一行結果：
若矩陣為對稱矩陣，輸出 YES。
若矩陣不是對稱矩陣，輸出 NO。
輸入限制
1 ≤ N ≤ 20
矩陣元素皆為整數，範圍為 -100～100。
輸入資料保證符合 N×N 的矩陣格式。
'''
def is_symmetric_matrix(double_list:list[list[int]])->bool:
  is_symmetric_matrix_bool = True
  flag = False

  for i in range(0, len(double_list)):
    for j in range(0, len(double_list)):
      if i == j:
        continue
      if double_list[i][j] != double_list[j][i]:
        is_symmetric_matrix_bool = False
        flag = True
        break
    if flag:
      break
  return is_symmetric_matrix_bool

def input_matrix_value()->list[list[int]]:
  matrix_size = int(input("輸入一個正整數 N，代表矩陣的列數與欄數"))

  double_list = []
  for i in range(0, matrix_size):
    row_list = []
    for j in range(0, matrix_size):
      nu = int(input(f"請輸入矩陣第[{i}][{j}]個元素數字:"))
      row_list.append(nu)
    double_list.append(row_list)
  return double_list

def c():
  matrix = input_matrix_value()
  print("原始矩陣:")
  for i in matrix:
    print(i)

  print(f'該矩陣{'是' if is_symmetric_matrix(matrix) else '不是'}對稱矩陣')


