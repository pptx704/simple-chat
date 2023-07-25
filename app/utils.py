from .const import NUM_PARTITIONS, NUM_TOPICS
from hashlib import md5

def custom_hash(key: str) -> int:
    return int(md5(key.encode()).hexdigest(), 16)

def get_topic_and_partition(chat_type: str, chat_id: str) -> tuple[str, int]:
    chat_id = custom_hash(chat_id)
    topic = f'{chat_type}-topic-{chat_id % NUM_TOPICS}'
    partition = (chat_id * custom_hash(chat_type)) % NUM_PARTITIONS
    return topic, partition

def list_tuple_to_dict(t: list[tuple[str, bytes]]) -> dict:
    return {k: v.decode() for k, v in t}