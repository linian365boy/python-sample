#!/usr/bin/env python
# coding=utf-8


"""
python 实现本地缓存
"""
import time


def main(value):
	main_name = '_'.join(main.__name__)
	main_name_time = main_name + '_time'
	cache_data = getattr(main, main_name, None)
	if not cache_data:
		# store value
		setattr(main, main_name, value)
		# store timeout
		setattr(main, main_name_time, int(time.time())+5)
		return ' no data %s ' % cache_data
	else:
		return cache_data


if __name__ == '__main__':
	str = main('hello world')
	print(str)
