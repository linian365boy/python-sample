

def main():
	sessionids = ['ab', 'bd', 'cg', 'de']
	INDEX_NAME = 'gameabr_%s_%s_%s.%s'
	index = ','.join('\''+INDEX_NAME % ('*', sessionid, 'report', '*'+'\'') for sessionid in sessionids)
	print(index)


if __name__ == '__main__':
	main()
