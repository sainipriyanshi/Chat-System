# Simple Object-Oriented Chat System (Python)

This project implements a simple, object-oriented chat system in Python. It features basic classes to represent **users**, **messages**, and **chat rooms**, allowing users to join or leave rooms, send messages, and review chat histories.

## Features

- **User System**: Users can join/leave any chat room and send messages.
- **Chat Rooms**: Rooms maintain their own user lists and message histories.
- **Message Broadcasting**: Sent messages are broadcast to the room and stored with unique message IDs.
- **Chat History**: Viewable transcript of all messages in each room.
- **Sample Usage**: The included example shows how to create users, rooms, and simulate a real conversation.

## Code Structure

- `Message`: Represents an individual message with unique ID and sender information.
- `User`: Represents a user who can join and leave chat rooms, as well as send messages.
- `ChatRoom`: Represents a chat room that holds users and a history of messages.

## Example

```python
# Create Users
alice = User("Alice")
bob = User("Bob")

# Create a ChatRoom
main_room = ChatRoom("Main Lobby")

# Users join the ChatRoom
alice.join_chatroom(main_room)
bob.join_chatroom(main_room)

# Users send messages
alice.send_message("Hello everyone!")
bob.send_message("Hi Alice!")

# Show chat history
main_room.show_chat_history()
```

This produces:

```
--------------------
(1) Alice: Hello everyone!
(2) Bob: Hi Alice!
--------------------
Chat History of Main Lobby:
(1) Alice: Hello everyone!
(2) Bob: Hi Alice!
```

## Getting Started

1. Clone this repository.
2. Run the `Chat System.py` script with Python 3.
3. Modify the example usage or expand the classes to add features such as private messaging, chatroom moderation, etc.

## License

This project is licensed under the MIT License.
