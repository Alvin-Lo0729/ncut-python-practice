import string

strValue=str(55.4)

print(strValue)

integerValue=str(1.0e4)
print(integerValue)

palindrome="A man,\nA plan,\na canal:\nPanama."

print(palindrome)


print('\tabc')
print('a\tbc')
print('ab\tc')
print('abc\t')

strValue1="abcd"+"bbb"
print(strValue1)

a="Duck"
b=a
c="Grey Duck"

print(a ,b,c)
start="Na "*4+"\n"
middle ="Hey!"*3+"\n"
end="Goodbye."
print(start,middle,end)

letters='abcdefghijklmnopqrstuvwxyz'
print(letters[0])
print(letters[1])
print(letters[2])
print(letters[-1])
print(letters[-2])

print(letters[0:4])

print(letters[:])

print(letters[20:])
print(letters[10:])
print(letters[12:15])
print(letters[-3:])
print(letters[18:-3])
print(letters[-6:-2])
print("letters[-2:-6]:"+letters[-2:-6])

print("letters[::7]:"+letters[::7])

print("letters[4:20:3]:"+letters[4:20:3])

print("letters[19::4]:"+letters[19::4])

print("letters[:21:5]:"+letters[:21:5])

print("letters[-1::-1]:"+letters[-1::-1])

print("letters[::-1]:"+letters[::-1])

print(len(letters))
empty=""
print(len(empty))

tasks="get gloves,get mask,give cat vitamins,call ambulance"
print(tasks.split(","))
print(tasks.split())

crypto_list=['Yeti','Bigfoot','Loch Ness Monster']
crypto_string=','.join(crypto_list)

print("Found and signing book deals:",crypto_string)

setup="a duck goes into a bar..."
print(setup.replace('duck','marmoset'))
print(setup)
print(setup.replace('a','the ',100))

world="   earth   "
print("world.strip():",world.strip())
print("world.strip(' '):",world.strip(' '))
print("world.lstrip():",world.lstrip())
print("world.rstrip():",world.rstrip())
print("world.rstrip('!'):",world.strip('!'))
print("string.whitespace",string.whitespace)
print("string.punctuation",string.punctuation)

poem="""All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die no doubt."""

print("poem[:13]:",poem[:13])
print(len(poem))

print(poem.title())


setup="a duck goes into a bar..."
print(setup.capitalize())
print(setup.title())
print(setup.upper())
print(setup.lower())
print(setup.swapcase())

print(setup.center(30))
print(setup.rjust(30))
print(setup.ljust(30))