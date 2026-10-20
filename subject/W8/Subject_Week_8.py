# my_hobbies=[]

# my_hobbies.append("看電影")
# my_hobbies.append("打電動")
# my_hobbies.append("聽音樂")
#
# print(my_hobbies)
#
# for i in range(0,3):
#   hobbie=input(f"請輸入你的第{(i+1)}個興趣:")
#   my_hobbies.append(hobbie)
#
# print(f"你的所有興趣為:{my_hobbies}")

queue=['陳先生','林小姐','黃先生']

name=input("請輸入等待者的姓氏：")
queue.append(name)

ok_name=queue.pop(0)
print(f"請{ok_name}，入座用餐")

print(f"目前還在排隊的有:{queue}")

aa=sorted(queue)
print(f"目前還在排隊的有:{aa}")
aa.reverse()
print(f"目前還在排隊的有:{aa}")

