# 使用for迴圈來印出串列[3,2,1,0]的值

for i in [3,2,1,0]:
    print(i)

guess_me=7
number=1

while True:
    if number > guess_me:
        print("oops")
        break
    elif number==guess_me:
        print("found it!")
        break
    else:
        print("too low")
    number+=1

guess_me=5

for number in range(10):
    if number<guess_me:
        print("too low")
    elif number==guess_me:
        print("found it!")
        break
    else:
        print("oops")
