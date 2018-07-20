#!/usr/bin/env python
# coding=utf-8

import logging as log

import datetime
import redis
import time

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

NOTIFY_USER_SIZE_PER_LOOP = 1000


def notify_check_in(cid, title, notice, url, voucher_code, image_info):
	"""
	notify user to check in, if user yesterday check in but today not check in
	:param cid: country/region
	:param title: title
	:param notice: notice message
	:param url: redirect url
	:param voucher_code:
	:param image_info:
	:param noticode: use lucky draw code
	:return: nil
	"""
	log.warn('###notify_check_in##cid=%s##title=%s##notice=%s##url=%s##', cid, title, notice, url)
	# 0、get the main notify switch is on or off from redis
	switch_status = r.get('clp_main_check_in_switch_dev_sg')
	start_time = time.time() * 1000
	if not switch_status or switch_status == 'on':
		# 1、get uids that yesterday check in from redis
		key = 'clp_user_check_in_uids_dev_sg_%s' % truncate_date_string(int(time.time())-86400)
		uids_size = r.zcard(key)
		loop_size = uids_size/NOTIFY_USER_SIZE_PER_LOOP \
			if (uids_size % NOTIFY_USER_SIZE_PER_LOOP == 0) else uids_size/NOTIFY_USER_SIZE_PER_LOOP + 1
		for i in range(loop_size):
			start = i * NOTIFY_USER_SIZE_PER_LOOP
			uids_list = r.zrange(key, start, start + NOTIFY_USER_SIZE_PER_LOOP - 1)
			if not uids_list:
				log.warn('###notify_check_in##get yesterday uids from redis is None##cid=%s##', cid)
				return
			uid_keys = []
			for uid in uids_list:
				uid_keys.append('clp_user_check_in_switch_dev_sg_%s' % uid)
			# 2、get the user switch is on or off from redis
			user_switch_status_dict = redis_dict(uid_keys)
			for uid in uids_list:
				user_switch_status = user_switch_status_dict.get('clp_user_check_in_switch_dev_sg_%s' % uid)
				if not user_switch_status or user_switch_status == 'on':
						#i = int(uid) + 1
						pass
						# query_server.notifiy_user(uid, title, notice, url, voucher_code, image_info, noticode)
						#log.warn('##notify_check_in_ok##uid=%s##title=%s##notice=%s##url=%s##voucher_code=%s
				# ##image_info=%s##')
				else:
					log.warn('###notify_check_in user notify switch is set off##cid=%s##uid=%s##', cid, uid)

		log.warning("cost time => {} ms".format(time.time() * 1000 - start_time))
	else:
		# the main notify switch is set off, not work
		log.warn('###notify_check_in main notify switch is set off##cid=%s##', cid)


def truncate_date_string(now=None):
	if type(now) is int or type(now) is float:
		now = datetime.datetime.fromtimestamp(now)
	if not now:
		now = datetime.datetime.now()
	return now.strftime('%Y-%m-%d')


def redis_dict(keys):
	values_list = r.mget(keys)
	values = {}
	for i in xrange(len(keys)):
		value = values_list[i]
		if value is not None:
			values[keys[i]] = value
	return values


if __name__ == '__main__':
	notify_check_in('sg', 'title', 'notice', 'http://www.baidu.com', '2000', 'image_info')
