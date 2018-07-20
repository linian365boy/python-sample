from pykafka import KafkaClient
from pykafka.common import OffsetType

client = KafkaClient(hosts='127.0.0.1:9092')
topic = client.topics['test_kafka']

consumer = topic.get_simple_consumer(
	consumer_group="test_mygroup",
	auto_offset_reset=OffsetType.LATEST,
)

print(consumer.consume())
print(consumer.commit_offsets())

consumer_2 = topic.get_simple_consumer(
	consumer_group="test_mygroup"
)
print(consumer_2.consume())
print(consumer_2.commit_offsets())


consumer_3 = topic.get_simple_consumer(
	consumer_group="test_mygroup",
	auto_offset_reset=OffsetType.EARLIEST,
	reset_offset_on_start=True
)
print(consumer_3.consume())
print(consumer_3.commit_offsets())



