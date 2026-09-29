def number_count(number1: int) -> int:
  if number1 <= 1:
    return 0

  counter_num = 0
  for x in (x1 for x1 in range(1, number1 + 1) if x1 % 2 == 0):
    counter_num += x

  return counter_num


def find_bad_score(score: int) -> int:
  return True if score < 60 else False


def count_score(score1: int, score2: int) -> int:
  return score2 - score1


def find_number_of_divisors(value: int) -> list[int]:
  list_value = []

  for x in (x1 for x1 in range(1, value + 1) if value % x1 == 0):
    list_value.append(x)

  return list_value


def find_number_of_max_divisors(value1: int, value2: int) -> int:
  max_divisors = 1
  for x in range(1, min(value1, value2) + 1):
    if value1 % x == 0 and value2 % x == 0:
      max_divisors = x

  return max_divisors


if __name__ == "__main__":
  # number = int(input("請輸入一個數字，自動計算從1到N之間（包含 N）所有「偶數」的相加總和"))
  # print(f'countNumber:{number_count(number)}')
  # num_map = {0: "零", 1: "一", 2: "二", 3: "三", 4: "四",
  #            5: "五", 6: "六", 7: "七", 8: "八", 9: "九"}
  # scores = [85, 42, 76, 58, 91, 39]
  #
  # for i in range(len(scores)):
  #   isBad=find_bad_score(scores[i])
  #   if isBad:
  #     print(f'第{num_map[(i+1)]}個學生，不及格，成績:{scores[i]}')

  # exam1 = [70, 85, 60, 90, 55]
  # exam2 = [80, 78, 75, 92, 70]
  # num_map = {0: "零", 1: "一", 2: "二", 3: "三", 4: "四",
  #            5: "五", 6: "六", 7: "七", 8: "八", 9: "九"}
  # for i in range(len(exam1)):
  #   sc = count_score(exam1[i], exam2[i])
  #   if sc > 0:
  #     print(f'第{num_map[(i + 1)]}個學生，第二次考試較第一次考試進步:{sc}分')
  # number = int(input("請輸入一個數字，幫你算他的公因數"))
  # list_value=find_number_of_divisors(number)
  # print(f'{number}的因數有:{list_value}，總共有{len(list_value)}個因數')

  print("幫你算最大公因數")
  number = int(input("請輸入第一個數字"))
  number2 = int(input("請輸入第二個數字"))
  vv = find_number_of_max_divisors(number, number2)
  print(f'{number} 、 {number2}最大公因數為：{vv}')
