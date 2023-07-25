import threading
from kafka import KafkaProducer, KafkaConsumer, TopicPartition

from .const import KAFKA_BROKER, GROUP
from .utils import get_topic_and_partition, list_tuple_to_dict

def listen_for_messages(consumer, room_topic, partition, room_name, user_name):
    last_offset = consumer.position(TopicPartition(room_topic, partition))
    consumer.seek(TopicPartition(room_topic, partition), max(0, last_offset - 10))
    for message in consumer:
        headers = list_tuple_to_dict(message.headers)
        if message.key.decode("utf-8") == room_name and headers["from"] != user_name:
            print(f"{headers['from']}: {message.value}")

def send_messages(producer, room_topic, partition, room_name, user_name):
    while True:
        message = input()
        if message.lower() == 'exit':
            break
        producer.send(room_topic, message, partition=partition, key=room_name.encode('utf-8'), headers=[("from", user_name.encode('utf-8'))])
        producer.flush()

def join_chat_room(room_name, user_name):
    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER, value_serializer=lambda v: v.encode('utf-8'))
    consumer = KafkaConsumer(bootstrap_servers=KAFKA_BROKER, value_deserializer=lambda v: v.decode('utf-8'))

    room_topic, partition = get_topic_and_partition(GROUP, room_name)

    consumer.assign([TopicPartition(room_topic, partition)])
    print(f"Joined chat room: {room_name} as {user_name}")

    thread = threading.Thread(target=listen_for_messages, args=(consumer, room_topic, partition, room_name, user_name))
    thread.daemon = True
    thread.start()

    send_messages(producer, room_topic, partition, room_name, user_name)

    producer.close()
    consumer.close()