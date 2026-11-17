'''
多條件自訂排序
情境說明
現有一份學生競賽成績的元組串列，每個元組包含 (姓名, 總分, 完賽時間秒數)。請依照以下規則進行排名：
scores = [
    ("Alice", 90, 120),
    ("Bob", 95, 150),
    ("Charlie", 90, 110),
    ("David", 90, 110)
]
總分高者排在前面（降冪）。
若總分相同，則完賽時間短者排在前面（升冪）。
若前兩者皆相同，則依照姓名字母順序排列（升冪）。
'''

def hw01():
  scores = [
    ("Alice", 90, 120),
    ("Bob", 95, 150),
    ("Charlie", 90, 110),
    ("David", 90, 110)
  ]

  ranked_scores = sorted(scores, key=lambda x: (-x[1], x[2], x[0]))

  for rank, item in enumerate(ranked_scores, start=1):
    print(f"第 {rank} 名: {item}")

'''
統計連續或重複出現最多次的座標
題目說明
在二維平面上有一系列機器人移動的座標紀錄 (x, y)。
請找出經過次數最多的座標，並印出 (座標, 次數) 的元組。
path = [(0, 0), (1, 0), (1, 1), (0, 0), (2, 1), (1, 1), (0, 0)]
'''
path = [(0, 0), (1, 0), (1, 1), (0, 0), (2, 1), (1, 1), (0, 0)]
vv = []
seen = []                      # 另外記錄已處理過的座標
for x in path:
    if x not in seen:
        seen.append(x)
        vv.append((x, path.count(x)))

kk=sorted(vv,key= lambda x:-x[1])

print(max(vv, key=lambda x: x[1]))



