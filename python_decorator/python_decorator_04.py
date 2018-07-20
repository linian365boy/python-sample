
def decorator_a(*args):
    print('Get in decorator_a=%s' % str(args))
    def args_fun(func):
	    def inner_a(*args, **kwargs):
	        print 'Get in inner_a'
	        return func(*args, **kwargs)
	    return inner_a
    return args_fun


def decorator_b(func):
	print ('Get in decorator_b=%s' % func.__name__)
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
@decorator_a(1, 2)
def f_01(x):
	print('Get in f_01')
	return x * 2


result_02 = f_01(1)
print(result_02)
