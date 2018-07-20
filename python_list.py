# -*- coding: utf-8 -*-


def main():
	lists = list()
	for x in xrange(100):
		lists.append(x)
	print(lists)

	for x in lists.__iter__():
		print(x)


if __name__ == '__main__':
	main()
	a = 2; print(a)
