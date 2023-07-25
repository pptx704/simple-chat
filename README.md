# simple-chat
simple-chat is a console based simple chat application using Apache Kafka. 

## Why?
The main reason is to try out Kafka for chat applications. Apart from that, I want to work on TUIs (probably `curses` or `pytermgui`). 

Am I rebuilding the wheel? Because nobody will use this, it doesn't matter.

## How to run?
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run Kafka using `docker-compose up --build`
4. Use `app.create_topics.create_topics()` function for first time use
5. Run `main.py` on multiple terminals to simulate multiple users
6. Join a chat room and start chatting!

## How does it work?
User puts a chatroom name and a username. A topic and partition is selected for that chatroom. The consumer then subscribes to the topic and partition and listens for messages on a thread. When user joins a chat with already existing messages, it polls the last 10 messages. For sending messages, the producer sends the message to the same topic and partition. 

I could create a new topic for each chatroom but didn't do that for simplicity. However, I might do that when I implement authentication and private messaging.

## Features
- [x] Chat rooms
- [x] Message history (upto 10 messages)
- [ ] TUI
- [ ] Authentication
- [ ] Private messages
- [ ] End-to-end encryption

## Contributing
Maybe don't. But if you want to, create a pull request. The project uses [MIT LICENSE](LICENSE) so you can fork and do whatever you want with it.