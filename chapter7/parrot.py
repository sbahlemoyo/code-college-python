##Using input function to get data from the user to use in your program. We can use it in the program by storing it in a variable

message = input("Tell me something, and i will repeat it back to you: ")
print(message)

#While loop
##Letting the user choose when to quit

prompt = "\nTell me something, and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)
    if message!= 'quit':#Prevents the program from printing the word quit when the user wants to exit the program.
        print(message)


###Using a flag

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)