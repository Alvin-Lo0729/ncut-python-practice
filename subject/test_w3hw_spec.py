from subject.W3HW import (what_kind_triangle, is_leap_year, find_big,
                          high_way_discount_by_identity)


class TestIsLeapYear:
  """請使用者輸入一個西元年份。依據西曆規則判斷是否為閏年。
  規則：年份若能被 4 整除但不能被 100 整除，
  或者能被 400 整除，即為閏年。"""

  def test_divisible_by_4_but_not_by_100_is_a_leap_year(self):
    assert is_leap_year(2028) is True

  def test_divisible_by_100_but_not_by_400_is_not_a_leap_year(self):
    assert is_leap_year(2100) is False

  def test_divisible_by_400_is_a_leap_year(self):
    assert is_leap_year(2800) is True

  def test_not_divisible_by_4_is_not_a_leap_year(self):
    assert is_leap_year(2139) is False


'''
【題目】請使用者輸入三個不一樣的整數，利用 if-elif-else 結構找出其中的最大值並輸出。
【預期輸出】（輸入 35, 12, 89）：最大值是: 89
'''


class TestFindBig:
  def test_returns_the_third_number_when_it_is_the_largest(self):
    assert find_big(35, 12, 89) == 89

  def test_returns_the_second_number_when_it_is_the_largest(self):
    assert find_big(35, 89, 12) == 89

  def test_returns_the_first_number_when_it_is_the_largest(self):
    assert find_big(89, 12, 35) == 89

  def test_returns_that_value_when_all_three_are_equal(self):
    assert find_big(89, 89, 89) == 89

  def test_finds_the_largest_even_when_all_numbers_are_negative(self):
    assert find_big(-1, -5, -9) == -1


'''
【題目】某高鐵購票系統規定：基礎票價為 1000 元。
請使用者輸入身分（可輸入：學生、老人、一般）。若為學生打 8 折，老人打 5 折，一般不打折。
最後詢問是否持有「會員卡」（輸入 Y 或 N），
若持有會員卡，可在上述折扣後的金額上再打 95 折（若沒折扣則是原價打 95 折）。請輸出最終票價。
【預期輸出】（輸入 學生 且會員卡輸入 Y）：您的最終票價為: 760.0 元
'''
class TestHighWayDiscountByIdentity:

  def test_a_senior_with_a_member_card_gets_both_discounts(self):
    assert high_way_discount_by_identity("老人", True) == 475

  def test_a_senior_without_a_member_card_pays_half_price(self):
    assert high_way_discount_by_identity("老人", False) == 500

  def test_a_student_with_a_member_card_gets_both_discounts(self):
    assert high_way_discount_by_identity("學生", True) == 760

  def test_a_student_without_a_member_card_pays_80_percent(self):
    assert high_way_discount_by_identity("學生", False) == 800

  def test_a_regular_passenger_with_a_member_card_pays_95_percent(self):
    assert high_way_discount_by_identity("一般人", True) == 950

  def test_a_regular_passenger_without_a_member_card_pays_full_price(self):
    assert high_way_discount_by_identity("一般人", False) == 1000

  def test_an_unrecognised_identity_pays_the_full_price(self):
    assert high_way_discount_by_identity("阿貓阿狗", False) == 1000

  def test_an_unrecognised_identity_still_gets_the_member_card_discount(self):
    assert high_way_discount_by_identity("阿貓阿狗", True) == 950

  def test_an_identity_must_match_exactly_or_it_loses_the_discount(self):
    # 「學生 」多一個空格就不算學生，會被當成一般票價收全額
    assert high_way_discount_by_identity("學生 ", False) == 1000

  def test_the_price_is_always_a_whole_number(self):
    assert isinstance(high_way_discount_by_identity("學生", True), int)


class TestWhatKindTriangle:
  """請使用者輸入三角形三邊長，判斷它是哪一種三角形。
  規則：任兩邊之和必須大於第三邊，否則不成三角形；
  三邊相等為等邊，其中兩邊相等為等腰，三邊皆不等為普通三角形。"""

  def test_three_equal_sides_make_an_equilateral_triangle(self):
    assert what_kind_triangle(3, 3, 3) == "這是等邊三角形"

  def test_the_first_two_sides_being_equal_makes_an_isosceles_triangle(self):
    assert what_kind_triangle(3, 3, 5) == "這是等腰三角形"

  def test_the_last_two_sides_being_equal_makes_an_isosceles_triangle(self):
    assert what_kind_triangle(5, 3, 3) == "這是等腰三角形"

  def test_the_outer_two_sides_being_equal_makes_an_isosceles_triangle(self):
    assert what_kind_triangle(3, 5, 3) == "這是等腰三角形"

  def test_three_different_sides_make_a_scalene_triangle(self):
    assert what_kind_triangle(3, 4, 5) == "這是普通三角形"

  def test_the_third_side_being_too_long_is_not_a_triangle(self):
    assert what_kind_triangle(1, 2, 5) == "這不是三角形"

  def test_the_first_side_being_too_long_is_not_a_triangle(self):
    assert what_kind_triangle(5, 1, 2) == "這不是三角形"

  def test_the_second_side_being_too_long_is_not_a_triangle(self):
    assert what_kind_triangle(1, 5, 2) == "這不是三角形"

  def test_two_sides_that_exactly_equal_the_third_are_flat_and_not_a_triangle(self):
    # 邊界值：1 + 2 剛好等於 3，會壓扁成一條線。
    # 這條測試守的是三角不等式必須用 > 而不是 >=
    assert what_kind_triangle(1, 2, 3) == "這不是三角形"

  def test_sides_of_length_zero_are_not_a_triangle(self):
    assert what_kind_triangle(0, 0, 0) == "這不是三角形"

  def test_negative_sides_are_not_a_triangle(self):
    assert what_kind_triangle(-1, -1, -1) == "這不是三角形"


'''
情境描述：請寫一個模擬語音助理的程式。

根據使用者輸入的指令變數 command，做出相對應的動作：

輸入 "play"：印出 "開始播放音樂"

輸入 "stop"：印出 "音樂已暫停"

輸入 "next"：印出 "切換至下一首歌曲"

輸入其他任何指令：一律印出 "抱歉，我聽不懂這個指令"

'''
class TestAiCommand:
  def test_play(self):
    assert ai_command