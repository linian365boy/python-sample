import Queue
import json
from pykafka import KafkaClient
from django.conf import settings
from pykafka.exceptions import MessageSizeTooLarge

if settings.LIVE:
	kafka_hosts = '10.65.228.192:9092,10.65.228.193:9092,10.65.228.194:9092'
else:
	kafka_hosts = '10.65.132.21:9092,10.65.132.22:9092,10.65.132.23:9092'


kafka_hosts = '127.0.0.1:9092'

client = KafkaClient(hosts=kafka_hosts, broker_version='1.0.0', use_greenlets=True)
# topic = client.topics[settings.TOPIC]


def send_message(producer, key, message):
	"""
	:param producer: pykafka producer
	:param key: key to decide partition
	:param message: json serializable object to send
	:return:
	"""
	data = json.dumps(message)
	try:
		producer.produce(data, partition_key='{}'.format(key))
	except Exception as e:
		# log.exception(e)
		pass


def send_message_with_delivery_report(producer, key, message, count):
	"""
		:param producer: pykafka producer
		:param key: key to decide partition
		:param message: json serializable object to send
		:return:
		"""
	data = json.dumps(message)
	try:
		producer.produce(data, partition_key='{}'.format(key))
		if count % 10 ** 2 == 0:
			while True:
				try:
					msg, exc = producer.get_delivery_report(block=False)
					if exc is not None:
						if type(exc) is not MessageSizeTooLarge:
							producer.produce(msg.value, partition_key='{}'.format(key))
						else:
							# log.error('Failed to delivery msg {}:{}'.format(msg.partition_key, repr(exc)))
							pass
				except Queue.Empty:
					break
	except Exception as e:
		# log.exception(e)
		pass
