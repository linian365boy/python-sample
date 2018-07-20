# -*- coding: utf-8 -*-

from functools import wraps

"""
玩转python 装饰器
"""


def dispatcher(func):
	print('dispatcher function invoke fun=>{fun}.'.format(fun=func.__name__))

	@wraps(func)
	def _swap(args, **kwargs):
		#print('args=>{}, kwargs=>{}'.format(args, kwargs))
		args()
		return func()
	return _swap


@dispatcher
def log():
	#print('log function invoke.')
	pass


def print_fun():
	return "hehe"


@log(print_fun)
def print_str(name, age):
	print('hello world name={}, age={}'.format(name, age))


if __name__ == '__main__':
	name = 'hehe'
	age = 12
	print_str(name, age=age)

	# logf = log(print_str)
	# print('logf result={}'.format(logf(name, age)))
	# print('print_str func name=>{}'.format(print_str.__name__))


