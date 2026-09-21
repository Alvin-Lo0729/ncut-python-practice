# a = int(input("請輸入三角形Ａ邊長"))
# b = int(input("請輸入三角形B邊長"))
# c = int(input("請輸入三角形C邊長"))
#
# if (a + b) > c and (b + c) > a and (a + c) > b:
#   if a == b == c:
#     print("這是等邊三角形")
#   elif a == b or b == c or c == a:
#     print("這是等腰三角形")
#   else:
#     print("這是普通三角形")
# else:
#   print("這不是三角形")
def is_leap_year(year_parmeter: int) -> bool:
  if (year_parmeter % 400) == 0 or (
      (year_parmeter % 4 == 0) and (year_parmeter % 100 != 0)):
    return True
  else:
    return False


year = int(input("請輸入年份，幫你判斷是不是閏年:"))
is_leap_year_bool = is_leap_year(year)
print(f'西元{year}年，{is_leap_year_bool}')


def findBig(a: int, b: int, c: int) -> int:
  if a > b and a > c:
      return a
  elif b > c:
    return b
  else:
    return c
