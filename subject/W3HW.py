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


def ai_command(param: str):
  match param:
    case "play":
      return "開始播放音樂"
    case "stop":
      return "音樂已暫停"
    case "next":
      return "切換至下一首歌曲"
    case _:
      return "抱歉，我聽不懂這個指令"


def park_ticket_price(identity: str, age: int) -> int:
  if "本市市民" in identity:
    if age >= 65:
      return 0
    return 100
  else:
    if age < 12:
      return 250
    return 500


def parking_fee(hours: int) -> int:
  if hours <= 0:
    return 0

  remaining=hours
  money = 0
  if remaining>0:
    billed=remaining if remaining<=2 else 2
    money+=billed*30
    remaining-=billed

  if remaining>0:
    billed=remaining if remaining<=3 else 3
    money+=billed*40
    remaining-=billed

  if remaining>0:
    money += remaining * 60

  if money > 300:
    money = 300

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

  # identity = input("請輸入你的身分(老人、學生、一般人)")
  # has_card = input("請問是否有會員卡(Y、N)").lower() == "y"
  # print(f'你的票價為:{high_way_discount_by_identity(identity, has_card)}')

  # action = input("請輸入AI撥放器的動作(play、stop、next)")
  # print(f'ai_command:{ai_command(action)}')
  #
  # identity = input("請輸入你的身分(外縣市遊客、本市市民)")
  # age = int(input("請輸入你的年齡"))
  # print(f'你的主題樂園票價為:{park_ticket_price(identity, age)}')

  parking_hour=int(input("請輸入停車時數"))
  print(f'你停了{parking_hour}小時，停車費共:{parking_fee(parking_hour)}')