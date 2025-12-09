def decimal_to_binary(n):
    x=""
    while n>1:
        x+=str(n%2)
        n//=2
    x+="1"
    print(x[::-1]);



print(decimal_to_binary(1))