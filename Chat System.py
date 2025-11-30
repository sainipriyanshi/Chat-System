# -------------------------------
# Message Class
# -------------------------------
class Message:
    # Class attribute to keep track of message ID
    message_counter = 1

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        
        # Assign ID and increment the counter
        self.id = Message.message_counter
        Message.message_counter += 1

    def __str__(self):
        # Returns a formatted string representation of the message
        return f"({self.id}) {self.sender.username}: {self.content}"

# -------------------------------
# User Class
# -------------------------------
class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None # Initialize with no chatroom

    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.username} is already in a chatroom.")
        else:
            # 1. Add user to the chatroom's user list
            chatroom.add_user(self)
            # 2. Assign the chatroom to the user's attribute
            self.chatroom = chatroom
            print(f"{self.username} joined {chatroom.name}")

    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom.")
        else:
            # 1. Remove user from the chatroom's user list
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name}")
            # 2. Clear the user's chatroom attribute
            self.chatroom = None

    def send_message(self, content):
        if not self.chatroom:
            print(f"{self.username} cannot send a message (not in a chatroom).")
        else:
            # Delegate the actual message creation/storage to the chatroom
            self.chatroom.broadcast(self, content)

# -------------------------------
# ChatRoom Class
# -------------------------------
class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []    # List of User objects in the room
        self.messages = [] # List of Message objects (history)

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        # Use a try-except block for safer removal in case the user isn't found
        try:
            self.users.remove(user)
        except ValueError:
            print(f"Error: {user.username} was not found in {self.name}.")

    def broadcast(self, sender, content):
        # Create a new Message object
        message = Message(sender, content)
        # Store the message in the history
        self.messages.append(message)
        
        # Display the message (simulating broadcasting to all users)
        print(message)

    def show_chat_history(self):
        print(f"\nChat History of {self.name}:")
        if not self.messages:
            print("No messages yet.")
            return
            
        for msg in self.messages:
            print(msg)

# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    # Create Users
    alice = User("Alice")
    bob = User("Bob")
    charlie = User("Charlie")

    # Create a ChatRoom
    main_room = ChatRoom("Main Lobby")
    tech_room = ChatRoom("Tech Talk")

    # Alice and Bob join the Main Lobby
    alice.join_chatroom(main_room)
    bob.join_chatroom(main_room)
    
    print("-" * 20)

    # Send messages
    alice.send_message("Hello everyone, this is Alice!")
    bob.send_message("Hey Alice! What's up?")
    
    print("-" * 20)
    
    # Charlie joins the Tech Talk room
    charlie.join_chatroom(tech_room)
    charlie.send_message("Checking out the new AI models.")
    
    print("-" * 20)

    # Bob leaves the Main Lobby
    bob.leave_chatroom()
    alice.send_message("Bob just left. Hope he comes back!")
    
    print("-" * 20)
    
    # Show history
    main_room.show_chat_history()
    tech_room.show_chat_history()