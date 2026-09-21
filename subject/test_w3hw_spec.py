from subject.W3HW import (what_kind_triangle, park_ticket_price, parking_fee, is_leap_year, find_big,
                          high_way_discount_by_identity, ai_command)


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

  def test_two_sides_that_exactly_equal_the_third_are_flat_and_not_a_triangle(
      self):
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
    assert ai_command("play") == "開始播放音樂"

  def test_stop(self):
    assert ai_command("stop") == "音樂已暫停"

  def test_next(self):
    assert ai_command("next") == "切換至下一首歌曲"

  def test_other(self):
    assert ai_command("test11123") == "抱歉，我聽不懂這個指令"

'''
【題目描述】某主題樂園的門票收費標準如下：

第一層分類（身分）：區分為「外縣市遊客」與「本市市民」。

第二層分類（年齡）：
外縣市遊客：全票 500 元；若年齡小於 12 歲則為兒童票 250 元。
本市市民：一律享市民優惠票 100 元，但如果年齡大於等於 65 歲則完全免費。
'''


class TestParkTicketPrice:
  """依身分與年齡計算門票價格。
  外縣市遊客：全票 500，未滿 12 歲為兒童票 250。
  本市市民：一律 100，但 65 歲（含）以上免費。"""

  # --- 外縣市遊客 ---
  def test_an_adult_visitor_from_another_city_pays_the_full_price(self):
    assert park_ticket_price("外縣市遊客", 30) == 500

  def test_a_child_visitor_from_another_city_pays_the_child_price(self):
    assert park_ticket_price("外縣市遊客", 8) == 250

  def test_a_visitor_aged_11_is_still_a_child(self):
    # 邊界值：「小於 12」不含 12，所以 11 歲仍是兒童票
    assert park_ticket_price("外縣市遊客", 11) == 250

  def test_a_visitor_aged_12_already_pays_the_full_price(self):
    # 邊界值：守住 < 不能寫成 <=
    assert park_ticket_price("外縣市遊客", 12) == 500

  def test_a_senior_visitor_from_another_city_gets_no_discount(self):
    # 65 歲免費只給本市市民，外縣市的長者仍是全票
    assert park_ticket_price("外縣市遊客", 70) == 500

  # --- 本市市民 ---
  def test_an_adult_resident_pays_the_resident_price(self):
    assert park_ticket_price("本市市民", 30) == 100

  def test_a_child_resident_also_pays_the_resident_price(self):
    # 題目寫「一律」享市民優惠，所以兒童票 250 不適用於市民
    assert park_ticket_price("本市市民", 8) == 100

  def test_a_resident_aged_64_still_pays_the_resident_price(self):
    # 邊界值：「大於等於 65」不含 64
    assert park_ticket_price("本市市民", 64) == 100

  def test_a_resident_aged_65_gets_in_for_free(self):
    # 邊界值：守住 >= 不能寫成 >
    assert park_ticket_price("本市市民", 65) == 0

  def test_a_senior_resident_gets_in_for_free(self):
    assert park_ticket_price("本市市民", 80) == 0

  # --- 不認得的身分：整組比照外縣市遊客 ---
  def test_an_unrecognised_identity_is_treated_as_a_visitor_from_another_city(self):
    assert park_ticket_price("阿貓阿狗", 30) == 500

  def test_an_unrecognised_child_also_gets_the_child_price(self):
    # 這條才是真正釘住決定的測試：
    # 若改成「不認得就一律收全票 500」，只有這一條會紅
    assert park_ticket_price("阿貓阿狗", 8) == 250


'''
【題目】某停車場採用分段累進計費，收費標準如下：

2 小時以內（含）：每小時 30 元。

超過 2 小時 ～ 5 小時（含）：超過的部分，每小時 40 元。

超過 5 小時以上：超過的部分，每小時 60 元。

當日最高收費上限：300 元（若計算出的總金額超過 300 元，以 300 元計）。

請設計一個程式，讓使用者輸入停車時數（整數），並計算出應付的總停車金額。

【注意事項】本題考「累進制（分段計費）」邏輯，不能直接用總時數乘以最高級距的單價。

例如停 6 小時，不能直接算 6 × 60。範例說明：

若輸入：6計算方式為：前 2 小時：2 × 30 = 60 元

第 3 到第 5 小時（共 3 小時）：3 × 40 = 120 元

超過 5 小時的部分（共 1 小時）：1 × 60 = 60 元

總計：60 + 120 + 60 = 240 元

【預期輸出】總計：240 元

'''


class TestParkingFee:
  """分段累進停車費。
  前 2 小時每小時 30；第 3~5 小時每小時 40；第 6 小時起每小時 60。
  當日總額上限 300 元。"""

  # --- 各級距的代表值 ---
  def test_not_parking_at_all_costs_nothing(self):
    assert parking_fee(0) == 0

  def test_one_hour_is_charged_at_the_first_tier_rate(self):
    assert parking_fee(1) == 30

  # --- 門檻 2 小時的邊界 ---
  def test_exactly_two_hours_is_still_all_first_tier(self):
    # 「2 小時以內（含）」的「含」：2 小時全部算 30 元
    assert parking_fee(2) == 60

  def test_the_third_hour_is_charged_at_the_second_tier_rate(self):
    # 60 + 40。若誤寫成一口價 3 × 40 = 120 就會紅
    assert parking_fee(3) == 100

  # --- 門檻 5 小時的邊界 ---
  def test_exactly_five_hours_ends_the_second_tier(self):
    # 「～5 小時（含）」的「含」：60 + 40×3
    # 同時證明第二級距是「每小時」累加，不是只收一次 40
    assert parking_fee(5) == 180

  def test_the_sixth_hour_is_charged_at_the_third_tier_rate(self):
    # 題目自己的範例：60 + 120 + 60
    # 若誤寫成一口價 6 × 60 = 360 就會紅
    assert parking_fee(6) == 240

  # --- 上限 300 的邊界（要自己算出來，題目沒直接給）---
  def test_seven_hours_lands_exactly_on_the_cap(self):
    # 累進算出來剛好 300，還沒被上限砍到
    assert parking_fee(7) == 300

  def test_eight_hours_is_cut_down_by_the_daily_cap(self):
    # 累進算出來是 360，這是上限第一次真正生效
    assert parking_fee(8) == 300

  def test_parking_all_day_never_costs_more_than_the_cap(self):
    assert parking_fee(24) == 300
