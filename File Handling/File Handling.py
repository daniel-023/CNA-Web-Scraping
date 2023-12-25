# File Handling
with open('demo.txt', 'r', encoding='utf-8') as file:
    text = file.read()

print(text)

new_text = "Just like reading a file in Python, there are a number of ways to write in a file in Python. Let us see " \
           "how we can write the content of a file using the write() function in Python."

with open('new.txt', 'w') as file:
    file.write(new_text)



