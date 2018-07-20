#!/usr/bin/env python
# coding=utf-8


def main(clicks_data):
	for key in clicks_data:
		pass


def erhuo(uid, username, **kwargs):
	print(uid)
	print("=========")
	print(username)
	print("=========")
	print(kwargs)


if __name__ == '__main__':
	clicks_data = ('clicks_share', 'clicks_share_u',
	               'clicks_game_result_share', 'clicks_game_result_share_u',
	               'clicks_rank_entrance', 'clicks_rank_entrance_u',
	               'clicks_rules_icon', 'clicks_rules_icon_u',
	               'clicks_bgm_icon', 'clicks_bgm_icon_u',
	               'clicks_ended_button', 'clicks_ended_button_u'
	               )
	main(clicks_data)

	kwargs = {'uid': -1, 'username': 'niange'}
	return_dict = {'error': 'wrong-call'}
	print(dict(kwargs, **return_dict))
	erhuo(**dict(kwargs, **return_dict))

	print('Request: {0!r}'.format('#$#FE345345'))


