def what_kind_triangle(a: int, b: int, c: int) -> str:
  if (a + b) > c and (b + c) > a and (a + c) > b:
    if a == b == c:
      return "這是等邊三角形"
    elif a == b or b == c or c == a:
      return "這是等腰三角形"
    else:
      return "這是普通三角形"
  else:
    return "這不是三角形"


def is_leap_year(year_parmeter: int) -> bool:
  if (year_parmeter % 400) == 0 or (
      (year_parmeter % 4 == 0) and (year_parmeter % 100 != 0)):
    return True
  else:
    return False


def find_big(side_a: int, side_b: int, side_c: int) -> int:
  if side_a >= side_b:
    if side_a >= side_c:
      return side_a
    else:
      return side_c
  elif side_b >= side_c:
    return side_b
  else:
    return side_c


def high_way_discount_by_identity(identity: str, has_member_card: bool) -> int:
  money = 1000
  match identity:
    case "老人":
      money *= 0.5
      money = int(money)
    case "學生":
      money *= 0.8
      money = int(money)

  if has_member_card:
    money *= 0.95
    money = int(money)
  return money


if __name__ == "__main__":
  # a = int(input("請輸入三角形Ａ邊長"))
  # b = int(input("請輸入三角形B邊長"))
  # c = int(input("請輸入三角形C邊長"))
  # what_kind_triangle(a, b, c)
  #
  # year = int(input("請輸入年份，幫你判斷是不是閏年:"))
  # is_leap_year_bool = is_leap_year(year)
  # print(f'西元{year}年，{is_leap_year_bool}')
  #
  # print(f'請輸入3個數字，幫你判別哪個最大')
  # a = int(input("請輸入第一個數字"))
  # b = int(input("請輸入第二個數字"))
  # c = int(input("請輸入第三個數字"))
  #
  # print(f'最大的數字為:{find_big(a, b, c)}')

  identity = input("請輸入你的身分(老人、學生、一般人)")
  has_card = input("請問是否有會員卡(Y、N)").lower() == "y"
  print(f'你的票價為:{high_way_discount_by_identity(identity, has_card)}')
