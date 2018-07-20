
def decorator_a(func):
    print 'Get in decorator_a, func name=%s' % func.__name__
    def inner_a(*args, **kwargs):
        print 'Get in inner_a'
        return func(*args, **kwargs)
    return inner_a


def decorator_b(func):
    print 'Get in decorator_b , func name=%s' % func.__name__
    def inner_b(*args, **kwargs):
        print 'Get in inner_b'
        return func(*args, **kwargs)
    return inner_b


def compose(*funs):
	def deco(f):
		for fun in reversed(funs):
			f = fun(f)
		return f
	return deco


@decorator_b
@decorator_a
def f(x):
    print 'Get in f'
    return x * 2


result_01 = f(1)
print(result_01)

print("============================")


def ff_1(x):
    print 'Get in f'
    return x * 2

result_03 = decorator_b(decorator_a(ff_1))(1)
print('result_03 = %s' % result_03)

print("============================")


@compose(decorator_b, decorator_a)
def f_01(x):
	print('Get in f_01')
	return x * 2


result_02 = f_01(1)
print(result_02)
