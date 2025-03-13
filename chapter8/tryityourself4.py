text_messages = ['Hey, how are you doing?', 'I\'m good thanks', 'How was your summer holiday?', 'It was fantastic, we spent most of it out on the lake swimming and fishing', 'That\'s fantastic to hear!' ]
# def show_messages(messages):
#     for message in messages:
#         print(message)

# show_messages(text_messages)

# sent_messages = []
# def send_messages(messages):
#     while text_messages:
#         pop_message = messages.pop(0)
#         print(pop_message)
#         sent_messages.append(pop_message)

# send_messages(text_messages)
# print(text_messages)
# print(sent_messages)
sent_messages = []
def send_messages(messages):
    while copy_messages:
        pop_message = messages.pop(0)
        print(pop_message)
        sent_messages.append(pop_message)
         
copy_messages = text_messages[:]
send_messages(copy_messages)
print(text_messages)


