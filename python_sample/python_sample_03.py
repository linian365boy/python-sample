
def count(n):
    x = 0
    while x < n:
        value = yield x
        if value is not None:
            print 'Received value: %s' %value
        x += 1

gen = count(5)
print(gen.next())

value = gen.send('Hello')
print('%s=type=%s' % (value, type(value)))
