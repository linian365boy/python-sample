#!/usr/bin/env python
# coding=utf-8

try:
	import logging
except:
	import logging

	class LogFilter():
		def main(self, record):
			print('hello world.')

logger = logging.getLogger('simple')
#stream = logging.StreamHandler()
logger.addHandler(logging.StreamHandler())
logger.debug('often makes a very good meal of %s', 'visiting tourists')
logger.info('代码是给人看的{heheda}'.format(heheda='牛逼咯'))
logger.warn('warn 警告级别来袭')
logger.warning('warning 警告级别来袭')
# logging.warning(logging.warn is logging.warning)
logger.warn('##LOGIN_TOKEN##%s##', 'token is wrong')
logger.warn('things is %s %s', 'life', '!')
logger.warn('things is %s', 'life')
#logger.warn('things is %s', 'life', exc_info=1)

