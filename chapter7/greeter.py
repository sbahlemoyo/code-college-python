#Writing clear prompts so the user knows exactly what kind of information you require from them

name = input("Please enter your name: ")
print(f"\nHello, {name}")

#Sometimes you will want to write a prompt thats longer than one line.You can assign your prompt to a variable and pass that variable to the input()function. This allows you to build your prompt over several lines, then write a clean input statement.
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name_2 = input(prompt)
print(f"\nHello, {name}")