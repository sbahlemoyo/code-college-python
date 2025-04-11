def show_messages(messages):
    for message in messages:
        print(message)

texts = ["Hey!", "How's it going?", "Don't forget to call!", "See you soon."]
show_messages(texts)

#sending messages
def send_messages(messages, sent_messages):
    while messages:
        msg = messages.pop(0)  # Remove from beginning
        print(f"Sending message: {msg}")
        sent_messages.append(msg)

texts = ["Hey!", "How's it going?", "Don't forget to call!", "See you soon."]
sent_texts = []

send_messages(texts, sent_texts)

print("\nOriginal list (texts):", texts)
print("Sent messages:", sent_texts)

#archived messages
def send_messages(messages, sent_messages):
    while messages:
        msg = messages.pop(0)
        print(f"Sending message: {msg}")
        sent_messages.append(msg)

original_texts = ["Hey!", "How's it going?", "Don't forget to call!", "See you soon."]
copied_texts = original_texts[:]  # Create a copy
sent_texts = []

send_messages(copied_texts, sent_texts)

print("\nOriginal list (still safe):", original_texts)
print("Copied list (now empty):", copied_texts)
print("Sent messages:", sent_texts)
