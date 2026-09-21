
account="admin"
password="1234"
user_input_account=input("請輸入帳號")


if user_input_account!=account:
  print("帳號錯誤")
else:
  user_input_password=input("請輸入密碼")
  if user_input_password==password:
    print("密碼正確")
  else:
    print("密碼錯誤")
