'''
車票優惠與身分雙重檢查
【題目】某高鐵購票系統規定：基礎票價為 1000 元。
請使用者輸入身分（可輸入：學生、老人、一般）。若為學生打 8 折，老人打 5 折，一般不打折。
最後詢問是否持有「會員卡」（輸入 Y 或 N），
若持有會員卡，可在上述折扣後的金額上再打 95 折（若沒折扣則是原價打 95 折）。請輸出最終票價。
【預期輸出】（輸入 學生 且會員卡輸入 Y）：您的最終票價為: 760.0 元
'''

identity = input("請輸入你的身分(老人、學生、一般人)")
has_card = input("請問是否有會員卡(Y、N)").lower() == "y"


money = 1000
if identity == "老人":
  money *= 0.5
  money = int(money)
elif identity == "學生":
  money *= 0.8
  money = int(money)

if has_card:
  money *= 0.95
  money = int(money)

print(f'你的票價為:{money}')