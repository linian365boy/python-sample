

def _main(**kwargs):
	print(kwargs)
	print(kwargs.get('name', '234'))


def main(**kwargs):
	_main(**kwargs)


if __name__ == '__main__':
	main(name='niubi', age=23, tuple=(1, 2, 3, 'he'))
	main(age=23, tuple=(1, 2, 3, 'he'))

	clicks_data = ('clicks_share', 'clicks_share_u',
	               'clicks_game_result_share', 'clicks_game_result_share_u',
	               'clicks_rank_entrance', 'clicks_rank_entrance_u',
	               'clicks_rules_icon', 'clicks_rules_icon_u',
	               'clicks_bgm_icon', 'clicks_bgm_icon_u',
	               'clicks_ended_button', 'clicks_ended_button_u'
	               )
	data = {}.fromkeys(clicks_data, 0)
	print(data)

	for k in clicks_data:
		print(k)




