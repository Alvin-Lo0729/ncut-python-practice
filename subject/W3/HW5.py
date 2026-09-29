'''
AI 語音助理指令（基礎 match-case 應用）
情境描述：請寫一個模擬語音助理的程式。

根據使用者輸入的指令變數 command，做出相對應的動作：

輸入 "play"：印出 "開始播放音樂"

輸入 "stop"：印出 "音樂已暫停"

輸入 "next"：印出 "切換至下一首歌曲"

輸入其他任何指令：一律印出 "抱歉，我聽不懂這個指令"

'''

action = input("請輸入AI撥放器的動作(play、stop、next)")
match action:
  case "play":
    action_str = "開始播放音樂"
  case "stop":
    action_str = "音樂已暫停"
  case "next":
    action_str = "切換至下一首歌曲"
  case _:
    action_str = "抱歉，我聽不懂這個指令"

print(f"AI撥放器的動作:{action_str}")
