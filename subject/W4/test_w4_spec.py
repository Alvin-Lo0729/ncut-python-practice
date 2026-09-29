
from subject.W4.W4HW import (number_count,find_bad_score,find_number_of_divisors,find_number_of_max_divisors)
"""
  數字範圍累加
  請撰寫一個 Python 程式，
  讓使用者可以從鍵盤輸入任意一個正整數N。
  程式必須利用 For 迴圈，
  自動計算從1到N之間（包含 N）
  所有「偶數」的相加總和，
  並在螢幕上輸出最終的加總結果。
  """
class TestW4NumberCount:


  def test_input_n(self):
    assert number_count(10) == 30

  def test_input_0(self):
    assert number_count(0) == 0


class TestW4FindBadScore:

  def test_bad_score(self):
    assert find_bad_score(60)==False

  def test_bad_score1(self):
    assert find_bad_score(59)==True

'''
找出因數並計算因數個數
【問題描述】請撰寫一個 Python 程式，
讓使用者輸入一個正整數 n，使用 for 迴圈找出 n 的所有因數，並計算總共有幾個因數。

【預期輸出結果】

   請輸入一個正整數 n：12

   12 的因數有：1, 2, 3, 4, 6, 12

   總共有 6 個因數。
'''

class TestW4FindNumberOfDivisors:

  def test_bad_score(self):
    assert find_number_of_divisors(12)==[1,2,3,4,6,12]

  def test_bad_score1(self):
    assert find_number_of_divisors(1)==[1]


'''
最大公因數
問題描述】請撰寫一個 Python 程式，讓使用者輸入兩個正整數 ，使用 for 迴圈找出兩數的最大公因數。

【預期輸出結果】

   請輸入一個正整數 a：12

   請輸入一個正整數 b：18

   最大公因數:6
'''

class TestW4FindNumberOfMaxDivisors:

  def test_bad_score(self):
    assert find_number_of_max_divisors()==6

