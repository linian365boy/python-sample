str = 'http://www.baiduc.com?a=123'
start = str.index('?')
print(start)
str = str[0:start]
print(str)

str = 'http://www.baiduc.com2342#frwer#aeswr'
start = str.index('#')
print(start)
str = str[0:start]
print(str)