import traceback
from common.logger import log

def div(a, b):
	try:
		a/b
	except Exception as e:
		log.exception(e)


def diver(b):
	return b


def hehe():
	div(2, 0)


def hehe_01() :
	hehe()


if __name__ == '__main__':
	hehe()
