'''
停車費累進計算系統
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

parking_hour = int(input("請輸入停車時數"))

money = 0
if parking_hour > 5:
  money += ((parking_hour - 5) * 60)

if parking_hour > 2:
  temp_hour = (3 if parking_hour > 5 else parking_hour - 2)
  money += (temp_hour * 40)

if parking_hour > 0:
  temp_hour = (2 if parking_hour > 2 else parking_hour)
  money += (temp_hour * 30)

if money > 300:
  money = 300

print(f"你停了{parking_hour}小時，停車費共:{money}")
