# -*- coding: utf-8 -*-


if __name__ == '__main__':
	data_dict = dict()
	data_dict = {'uid': 1, 'username': 'nihao'}
	print(data_dict. has_key('uid'))
	print(data_dict['uid'])
	print(data_dict.get('uid'))
	print(data_dict['username'])
	print(data_dict.get('username'))
	print('uid=>{uid}, username=>{username}'.format(uid=data_dict.get('uid'), username=data_dict.get('username')))
	print('uid=>{uid}, username=>{username}'.format(
		**{'uid': data_dict.get('uid'), 'username': data_dict.get('username')}))
	print('uid=>{0}, username=>{1}'.format(data_dict.get('uid'), data_dict.get('username')))
	print('uid=>{0}, username=>{1}'.format(data_dict.get('uid'), data_dict.get('username')))
	print('uid=>{1}, username=>{0}'.format(data_dict.get('uid'), data_dict.get('username')))
	print(data_dict.get('title'))
	print(data_dict.get('title', 'niubilo'))

	id = 10
	if 9 < id < 11:
		print(False == False == False)
		print('nihao')
	else:
		print('nima')
