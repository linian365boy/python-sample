class Parent(object):
	def __init__(self):
		print('I am enter Parent')
		self.code = 100
		self.error_message = 'no message'
		self.response_code = 200


class aChild(Parent):
	def __init__(self):
		super(Parent, self).__init__()
		print('I am enter aChild')
		self.response_code = 205


class bChild(aChild):
	def __init__(self):
		super(aChild, self).__init__()
		print('I am enter bChild')
		self.response_code = 204


class cChild(bChild):
	def __init__(self):
		super(bChild, self).__init__()
		print('I am enter cChild')
		self.response_code = 203


class dChild(cChild):
	def __init__(self):
		super(bChild, self).__init__()
		print('I am enter dChild')
		self.response_code = 202

class eChild(dChild):
	def __init__(self):
		print('I am enter eChild')
		super(eChild, self).__init__()


if __name__ == '__main__':
	e_child = eChild()
	print(e_child.response_code)