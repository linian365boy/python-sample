from python_cycle_invoke import python_02


def aa():
	python_02.b()


def bb():
	python_02.c()


def cc():
	print('cc')


if __name__ == '__main__':
	aa()
