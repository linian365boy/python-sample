ALLOWED_REGION_LIST = ['ID', 'MY', 'PH', 'SG', 'TH', 'TW', 'VN']

CELERYBEAT_SCHEDULE_HEARTBEAT = {
	'task_heartbeat_%s' % cid.lower(): {
		'task': 'period',
		'schedule': '123',
		'options': {'queue': 'shopee_celery_clp_period_tasks_%s' % cid.lower()},
		'args': (cid, ),
	} for cid in ALLOWED_REGION_LIST
}

CELERYBEAT_SCHEDULE_CHECK_IN = {
		'period_notify_user_check_in_%s' % cid.lower(): {
			'task': 'notify_check_in',
			'schedule': '456',
			'options': {'queue': 'shopee_celery_clp_period_tasks_%s' % cid.lower()},
			'args': (cid,),
		} for cid in ALLOWED_REGION_LIST
	}

CELERYBEAT_SCHEDULE = dict(CELERYBEAT_SCHEDULE_HEARTBEAT, **CELERYBEAT_SCHEDULE_CHECK_IN)

print(CELERYBEAT_SCHEDULE)