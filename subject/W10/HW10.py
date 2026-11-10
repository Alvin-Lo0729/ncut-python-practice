from enum import Enum

class AnalysisType(Enum):
  English_word_count_number = "e_count",
  Number_word_count_number = "number_count",
  Other_word_count_number = "o_count",
  Alphabet_a_word_count_number = "alphabet_a"


'''
統計英文字母的次數:1
統計數字字元的數量:2
其他字元的數量:3
英文字母 a 出現的次數:4
'''


def count_str_number(input_value: str) -> dict:
  return_value = {AnalysisType.English_word_count_number: 0,
                  AnalysisType.Number_word_count_number: 0,
                  AnalysisType.Other_word_count_number: 0,
                  AnalysisType.Alphabet_a_word_count_number: 0}
  for a in input_value:
    if a.isalpha():
      return_value[AnalysisType.English_word_count_number] += 1
    if a.isdigit():
      return_value[AnalysisType.Number_word_count_number] += 1
    if not a.isalnum():
      return_value[AnalysisType.Other_word_count_number] += 1
    if a.lower() == 'a':
      return_value[AnalysisType.Alphabet_a_word_count_number] += 1

  return return_value


def analysis_str_fn():
  analysis_str = input("請輸入要被分析的字串")

  rv = count_str_number(analysis_str)

  print(
      f'英文字母有{rv[AnalysisType.English_word_count_number]}個\n數字有{rv[AnalysisType.Number_word_count_number]}個\n其他字元有{rv[AnalysisType.Other_word_count_number]}個\n字母 a 出現{rv[AnalysisType.Alphabet_a_word_count_number]}次')




def analysis_password(pw:str)->bool:
  if not(8<=len(pw)<=16):
    return False
  check_value=True
  has_big_alphabet = False
  has_little_alphabet = False
  has_any_number = False
  for x in pw:
    if not (x.isalnum()):
      return False
    if x.isnumeric():
      has_any_number=True
    if not has_big_alphabet and x.isupper():
      has_big_alphabet=True
    if not has_little_alphabet and x.islower():
      has_little_alphabet=True

  return has_big_alphabet and has_little_alphabet and has_any_number


pw_input=input("請輸入密碼，確認是否符合條件")
print(f'{"Valid" if analysis_password(pw_input) else "Invalid"}')