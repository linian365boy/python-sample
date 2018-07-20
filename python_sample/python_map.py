
def f(x):
	return x * x


r = map(f, [3, 4, 5, 6, 7, 8, 9])
print('r=%s, type=%s' % (r, type(r)))
l_ist = list(r)
print(l_ist)


list1 = map(str, [3, 4, 5, 6, 7, 8, 9])
print(list1)


