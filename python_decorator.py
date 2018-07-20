# -*- coding: utf-8 -*-

from functools import wraps

"""
玩转python 装饰器
"""


def log(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		print('args={args}, kwargs={kwargs}'.format(args=args, kwargs=kwargs))
		return f(*args, **kwargs)
	return wrap


@log
def print_str(name, age):
	print('hello world name={}, age={}'.format(name, age))


if __name__ == '__main__':
	name = 'hehe'
	age = 12
	print_str(name, age=age)

	# logf = log(print_str)
	# print('logf result={}'.format(logf(name, age)))
	print('print_str func name=>{}'.format(print_str.__name__))


