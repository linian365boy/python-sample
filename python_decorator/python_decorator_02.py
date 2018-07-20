
def decorator_a(*args):
    print('Get in decorator_a=%s' % str(args))
    def args_fun(func):
	    print ('Get in decorator_a args_fun=%s' % func.__name__)
	    def inner_a(*args, **kwargs):
	        print 'Get in inner_a'
	        return func(*args, **kwargs)
	    return inner_a
    return args_fun


def decorator_b(*args):
	print ('Get in decorator_b=%s' % args)
	def args_fun(func):
		print ('Get in decorator_b args_fun=%s' % func.__name__)
		def inner_b(*args, **kwargs):
			print 'Get in inner_b'
			return func(*args, **kwargs)
		return inner_b
	return args_fun


def compose(*funs):
	def deco(f):
		for fun in reversed(funs):
			f = fun(f)
		return f
	return deco


@compose(decorator_b('hehe'), decorator_a(1, 2))
def f_01(x):
	print('Get in f_01')
	return x * 2


result_02 = f_01(1)
print(result_02)


print("===========================")


@decorator_b('hehe')
@decorator_a(1, 2)
def f(x):
	print('Get in f')
	return x * 2


result = f(1)
print(result)
