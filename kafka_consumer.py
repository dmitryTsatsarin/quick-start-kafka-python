import msgpack
from kafka import KafkaConsumer

consumer = KafkaConsumer(value_deserializer=msgpack.loads, bootstrap_servers=['localhost:9092'],
                         # auto_offset_reset='earliest', enable_auto_commit=False
                         )
consumer.subscribe(['msgpack-topic'])

for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))
