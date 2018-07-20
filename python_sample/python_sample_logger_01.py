import logging
import os
from common.logger import log
from common.loggingmp import MPTimedRotatingFileHandler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOGGER_CONFIG = {
	'log_dir': os.path.join(os.path.dirname(BASE_DIR), 'log'),
}

log_dir = LOGGER_CONFIG['log_dir']


def add_extra_logger_if_not_exist(extra_logger, logger_config):
	handler = MPTimedRotatingFileHandler(**logger_config['handler'])
	handler.setFormatter(logging.Formatter(**logger_config['formatter']))
	logger = logging.getLogger(extra_logger)
	logger.setLevel(logger_config['level'])
	logger.addHandler(handler)
	setattr(log, extra_logger, logger.info)


def _patch_logger():
	extra_logger_config = {
		'dev': {
			'handler': {
				'filename': os.path.join(log_dir, 'dev-debug.log').replace('\\','/'),
				'when': 'MIDNIGHT',
				'backupCount': 30,
			},
			'formatter': {
				'fmt': '%(asctime)s.%(msecs)03d|%(levelname)s|%(process)d:%(thread)d|%(filename)s:%(lineno)d|%(module)s.%(funcName)s|%(message)s',
				'datefmt': '%Y-%m-%d %H:%M:%S',
			},
			'level': 'DEBUG',
		},
		'access': {
			'handler': {
				'filename': os.path.join(log_dir, 'access.log').replace('\\','/'),
				'when': 'MIDNIGHT',
				'backupCount': 30,
			},
			'formatter': {
				'fmt': '%(asctime)s.%(msecs)03d|%(levelname)s|%(process)d:%(thread)d|%(filename)s:%(lineno)d|%(module)s.%(funcName)s|%(message)s',
				'datefmt': '%Y-%m-%d %H:%M:%S',
			},
			'level': 'INFO',
		},
	}

	for extra_logger, logger_config in extra_logger_config.items():
		add_extra_logger_if_not_exist(extra_logger, logger_config)


_patch_logger()

log.access('I am coming...')

nian_access_log = logging.getLogger('access')
nian_dev_log = logging.getLogger('dev')
nian_main_log = logging.getLogger('main')
nian_data_log = logging.getLogger('data')
nian_tornado_general_log = logging.getLogger('tornado.general')

nian_access_log.warning('heheda, in the world. modou is very good...')
nian_dev_log.info('heheda, this is midou.I love it.')
nian_dev_log.warning('is not gengen...')
nian_dev_log.error('I am error.. thanks a lot.')

nian_main_log.info('use main log info level to log...')
nian_main_log.warning('use main log warning lever to log...')
nian_main_log.error('use main log error level to log...')

nian_data_log.info('use data log info level to log...')
nian_data_log.warning('use data log warning level to log...')
nian_data_log.error('use data log error level to log...')


nian_tornado_general_log.debug('use tornado general debug level to log...')
nian_tornado_general_log.info('use tornado general info level to log...')
nian_tornado_general_log.warning('use tornado general warning level to log...')
nian_tornado_general_log.error('use tornado general error level to log...')








