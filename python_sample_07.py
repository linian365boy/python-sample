# -*- coding: utf-8 -*-
import re


def clean_str(str):
	reg_str = '[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+'
	return re.sub(reg_str.decode('utf8'), ' '.decode('utf8'), str)


def clean_str_2(str):
	reg_str = r'[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+'
	return re.sub(reg_str, '', str)


def validate_email(email):
	reg_str = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
	return re.match(reg_str, email)


def f(**kwargs):
	print(kwargs)


if __name__ == '__main__':
	str = clean_str(u'    @#fgeUU#345$)#$点 击ert345发ert送6457欧567舒丹ert发   ')
	print('str=%s' % str)
	str_2 = clean_str_2(u'   @#fgeUU#345$)#$点 击ert345发ert送6457欧567舒丹ert发   ')
	print('str_2=%s' % str_2)
	vali_result = validate_email('2343511.com')
	print('vali_result=%s' % vali_result)
	print('   fd   '.strip())

	email = ''
	print('hehe=%s' % validate_email(email))

	kwargs = {'uid': 1, 'un': 'heheda'}
	f(**kwargs)
	f(**{'uid': 1, 'un': 'heheda'})

	str = clean_str(u'my  %%%%  name  %^&*  is  =-=-  lilei.').strip()
	print(str)
	str = u'&*(#*$#$#'
	str = clean_str(str).strip()
	print('==='+' '.join(str.split()))
