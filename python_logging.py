#!/usr/bin/env python
# coding=utf-8

import logging
from logging.config import dictConfig

logging_config = dict(
	version=1,
	formatters={
		'f': {
			'format':
				'%(asctime)s %(name)-10s %(lineno)d %(process)d %(thread)d %(threadName)s %(levelname)-8s %('
		                'message)s'}
	},
	handlers={
		'h': {'class': 'logging.FileHandler',
		      'filename': 'logging.log',
		      'formatter': 'f',
		      'level': logging.DEBUG
		      },
		'console': {
			'class': 'logging.StreamHandler',
			'level': 'DEBUG',
			'formatter': 'f'
		}
	},
	loggers={
		'root': {
			'handlers': ['console'],
			'level': 'DEBUG',
			# 'propagate': True,
		},
		'simple': {
			'handlers': ['console', 'h'],
			'level': 'WARN',
		}
	}
)

dictConfig(logging_config)

logger = logging.getLogger('simple')
logger.debug('often makes a very good meal of %s', 'visiting tourists')
logger.info('代码是给人看的{heheda}'.format(heheda='牛逼咯'))
logger.warn('warn 警告级别来袭')
logger.warning('warning 警告级别来袭')
# logging.warning(logging.warn is logging.warning)
logger.warn('##LOGIN_TOKEN##%s##', 'token is wrong')
logger.warn('things is %s %s', 'life', '!')
logger.warn('things is %s', 'life')
logger.warn('things is %s', 'life', exc_info=1)

logger2 = logging.getLogger('heheda')
logger2.error('test error message.')
