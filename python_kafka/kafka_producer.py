import time
from pykafka import KafkaClient

'''
client = KafkaClient(hosts='kafka-shopee-nonlive-10-65-132-21:9092,'
						   'kafka-shopee-nonlive-10-65-132-22:9092,'
						   'kafka-shopee-nonlive-10-65-132-23:9092')
'''

client = KafkaClient(hosts='127.0.0.1:9092', broker_version='1.0.0')
topic = client.topics['auto_create_kafka_topic']

start = int(time.time() * 1000)
with topic.get_sync_producer() as producer:
	for i in range(4):
		producer.produce('test message ' + str(i ** 3))
print('1 cost time => {time} ms'.format(time=int(time.time() * 1000) - start))
