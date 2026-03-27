# 1.使用for迴圈來印出串列[3,2,1,0]的值

# for number in range(3,-1,-1):
#   print(number)

#2
# guess_me=7
# number=1
#
# while True:
#   print(f"number is {number} and guess_me is {guess_me}")
#   if number>guess_me:
#     print("oops");
#
#   if number==guess_me:
#     print("Found it!")
#     break
#
#   if number< guess_me:
#     print("too low")
#
#   number+=1

#3.
guess_me =5
for number in range(10):
  print(f"number is {number} and guess_me is {guess_me}")
  if number>guess_me:
    print("oops");

  if number==guess_me:
    print("Found it!")
    break

  if number< guess_me:
    print("too low")



