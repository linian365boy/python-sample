
def main(name):
	str = name or '/'
	return str


if __name__ == '__main__':
	print(main('name hello'))
	print(main(''))
