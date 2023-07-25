import os

KAFKA_BROKER = os.environ.get('KAFKA_BROKER', 'localhost:9093')
NUM_PARTITIONS = int(os.environ.get('NUM_PARTITIONS', 3))
NUM_TOPICS = int(os.environ.get('NUM_TOPICS', 3))
REPLICATION_FACTOR = int(os.environ.get('REPLICATION_FACTOR', 1))
CLIENT_ID = os.environ.get('CLIENT_ID', 'kafka-python-admin')

GROUP = "group"