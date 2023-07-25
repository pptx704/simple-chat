import kafka

from .const import NUM_TOPICS, NUM_PARTITIONS, KAFKA_BROKER, CLIENT_ID, REPLICATION_FACTOR, GROUP

def create_topics():
    # Create a Kafka client instance.
    client = kafka.KafkaAdminClient(
        bootstrap_servers=KAFKA_BROKER,
        client_id=CLIENT_ID
    )

    # check if topics already exist
    topic_list = client.list_topics()
    if len(topic_list) > 0:
        print('Topics already exist. Exiting.')
        return
    
    # Create a list of TopicPartitions to be created.
    new_topics = [
        kafka.admin.NewTopic(
            name=f'{chat_type}-topic-{i}',
            num_partitions=NUM_PARTITIONS,
            replication_factor=REPLICATION_FACTOR
        ) for i in range(NUM_TOPICS) for chat_type in [GROUP]
    ]

    # Create the new topics using the client instance.
    client.create_topics(new_topics)
    print(f'Created {NUM_TOPICS} topics.')