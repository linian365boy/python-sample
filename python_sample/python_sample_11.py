ALLOWED_REGION_LIST = ['ID', 'MY', 'PH', 'SG', 'TH', 'TW', 'VN']

'''
CELERYBEAT_SCHEDULE = {
	{
		'task_heartbeat_%s' % cid.lower(): {
			'task': 'period',
			'schedule': '',
			'options': {'queue': 'shopee_celery_clp_period_tasks_%s' % cid.lower()},
			'args': (cid, ),
		},
		'period_notify_user_check_in_%s' % cid.lower(): {
			'task': 'notify_check_in',
			# default 'schedule': crontab(minute=0, hour=20),
			'schedule': '',
			'options': {'queue': ''},
			'args': (cid, 'title', 'notice', 'url', 'voucher_code', 'image_info'),
		}
	} for cid in ALLOWED_REGION_LIST
} 
'''


CELERYBEAT_SCHEDULE_1 = {
		'task_heartbeat_%s' % cid.lower(): {
			'task': 'period',
			'schedule': '',
			'options': {'queue': 'shopee_celery_clp_period_tasks_%s' % cid.lower()},
			'args': (cid, ),
		} for cid in ALLOWED_REGION_LIST
	}


CELERYBEAT_SCHEDULE = {
		'period_notify_user_check_in_%s' % cid.lower(): {
			'task': 'notify_check_in',
			# default 'schedule': crontab(minute=0, hour=20),
			'schedule': '',
			'options': {'queue': ''},
			'args': (cid, 'title', 'notice', 'url', 'voucher_code', 'image_info'),
		} for cid in ALLOWED_REGION_LIST
}

CELERYBEAT_SCHEDULE = dict(CELERYBEAT_SCHEDULE, **CELERYBEAT_SCHEDULE_1)


CELERYBEAT_SCHEDULE_02 = {
	'period_notify_user_check_in_tw': {
		'task': 'notify_check_in',
		'options': {'queue': ''},
		'args': ('TW', 'title', 'notice', 'url', 'voucher_code', 'image_info'),
		'schedule': ''
	},
	'period_notify_user_check_in_vn': {
		'task': 'notify_check_in',
		'options': {'queue': ''},
		'args': ('VN', 'title', 'notice', 'url', 'voucher_code', 'image_info'),
		'schedule': ''
	},
	'period_notify_user_check_in_sg': {
		'task': 'notify_check_in',
		'options': {'queue': ''},
		'args': ('SG', 'title', 'notice', 'url', 'voucher_code', 'image_info'),
		'schedule': ''
	}
}


print(CELERYBEAT_SCHEDULE)

