from datetime import datetime
import time
import pytz
from elasticsearch import Elasticsearch

ELASTICSEARCH_COINS_CONFIG = [
	{'host': '127.0.0.1', 'port': '9200'},
	]


global_es_client = Elasticsearch(ELASTICSEARCH_COINS_CONFIG)
now = time.time()
now_date = datetime.fromtimestamp(now, pytz.timezone('Asia/Singapore'))
year_month_day = now_date.strftime('%Y%m%d')


def es_index():
	index = "gameabr_id_dev_32_192_play.%s" % year_month_day
	body = {
		"eventid": 32,
		"status": "ended",
		"stats_lucky_hist": [],
		"ip_addr": "61.244.187.135",
		"coins_limit": 1000,
		"coreserver_rollback": "[]",
		"ip": "61.244.187.135",
		"start_time": 1529489100,
		"lucky": True,
		"sessionid": 192,
		"devicetype": "pc",
		"game_id": 0,
		"now": 1529489305,
		"final_times": 0,
		"logid": "14066202042760015294892051599765",
		"core_server_track": "{}",
		"ignore": False,
		"logts": 1529489205,
		"noti_result": "{}",
		"geo": {
			"location": "52.5720661,52.5720661"
		},
		"coins": 120,
		"userid": 12345678,
		"times": 12,
		"username": "mkttestingo39",
		"end_time": 1529596800,
		"session_name": "test natural end",
		"@timestamp": "2018-06-20T18:09:45.201228",
		"deviceid": "VDKOrTmqNfE3Gb9cDSafi5cAl6B7v3MoV",
		"delivery": True,
		"bonus": 0,
		"bonus_type": "",
		"bonus_type_value": "0",
		"total_coins": 120,
		"group_id": "0",
		"group_all": "",
		"group_full": False
	}
	result = global_es_client.index(index=index, body=body, doc_type='default')
	return result


if __name__ == '__main__':
	result = es_index()
	print('es index result=%s' % result)
