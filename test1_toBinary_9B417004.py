def decimal_to_binary(n:int) ->str:
    x=""
    while n>1:
        x+=str(n%2)
        n//=2
    x+="1"
    return x[::-1]



print(decimal_to_binary(11))