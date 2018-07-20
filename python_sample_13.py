#!/usr/bin/env python
# coding=utf-8


def main():
	from datetime import datetime
	now = datetime.now()
	print(now)
	print(type(now))
	epoch = datetime(1970, 1, 1)
	diff = now - epoch
	print(type(diff))
	print(diff.total_seconds())
	print diff.total_seconds()
	print "Hello World"
	'''
	while True:
		try:
			x = int(raw_input('please enter a number: '))
			break
		except ValueError:
			print('Oops! That was not valid number. try again...')
	'''

	str = '''heheda
					niujd'''
	print(str)

	try:
		x = int(raw_input('please enter a number: '))
	except ValueError:
		print('Oops! That was not valid number. try again...')
	else:
		print('x={x} enter else.'.format(x=x))


if __name__ == '__main__':
	main()
