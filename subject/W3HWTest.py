from subject.W3HW import is_leap_year


class TestIsLeapYear:
  """請使用者輸入一個西元年份。依據西曆規則判斷是否為閏年。
  規則：年份若能被 4 整除但不能被 100 整除，
  或者能被 400 整除，即為閏年。"""

  def test1(self):
    assert is_leap_year(2028) is True

  def test2(self):
    assert is_leap_year(2100) is False

  def test3(self):
    assert is_leap_year(2800) is True

  def test4(self):
    assert is_leap_year(2139) is False


'''
【題目】請使用者輸入三個不一樣的整數，利用 if-elif-else 結構找出其中的最大值並輸出。
【預期輸出】（輸入 35, 12, 89）：最大值是: 89
'''

class TestFindBig:
  def test1(self):
    assert findBig(35,12,89) is 89