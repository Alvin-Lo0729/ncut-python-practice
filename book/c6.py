# count=1
#
# while count<=20:
#     print("Count is: %d " % count)
#     count+=1
#     if count==15:
#         break
#
#
# while True:
#     stuff=input("String to capitalize [type q to quit]: ")
#     if stuff=="q":
#         break
#     print(stuff.capitalize())
#
#
# while True:
#     value=input("Integer,please [q to quit]: ")
#     if value=="q": #退出
#         break
#     number=int(value)
#     if number%2==0:
#         continue
#     print(number, "squared is", number*number)
#
# numbers=[1,3,5,7,11,9]
# position=0
# while position < len(numbers):
#     number=numbers[position]
#     print("Testing number", number)
#     # if(number%2)==0:
#     #     print("Found even number", number)
#     #     break
#     if number==9:
#         print("Found number 9")
#         break
#     position+=1
# else:
#     print("No even number found")
#
# word="letters"
# offset=0
# while offset< len(word):
#     print(word[offset])
#     offset+=1
# print("=====================================")
# for a in word:
#     if a=="t":
#         continue
#
#     print(a)
# else:
#     print(a)


for x in range(0,10):
    print(x)

print(list(range(0,10)))

for x in range(50,-1,-5):
    print(x)