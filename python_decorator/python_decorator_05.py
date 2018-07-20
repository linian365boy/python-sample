import logging


def hello_wrap(func):
	def _wrap(*args, **kwargs):
		result = func(*args, **kwargs)
		# do something start
		try:
			div = 1/0
		except:
			logging.error("i happend error.")
		# do end
		return result
 	return _wrap


@hello_wrap
def hello(uid, name, age):
	if age > 100:
		raise Exception("you age is too large.")
	uid = uid + 100
	name = 'hello.' + name
	return uid, name, age

result_hello = hello(1, 'niange', 100)

print(result_hello)

