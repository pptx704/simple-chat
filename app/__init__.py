from .chat import join_chat_room

def start_chat():
    room_name = input("Enter room name: ")
    user_name = input("Enter user name: ")
    join_chat_room(room_name, user_name)