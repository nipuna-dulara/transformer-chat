import re

# Read the chat data from the text file
with open('_chat.txt', 'r', encoding='utf-8') as file:
    chat_lines = file.readlines()

# Define a regular expression pattern to match the chat lines
pattern = r'\[\d{4}-\d{2}-\d{2}, \d{2}:\d{2}:\d{2}\] (\w+): (.*)'

# Process and extract chat messages
chat_messages = []
for line in chat_lines:
    match = re.match(pattern, line)
    if match:
        sender = match.group(1)
        message = match.group(2)
        chat_messages.append(f"{sender}: {message}")

# Save the cleaned chat messages to a new file
with open('chat.txt', 'w', encoding='utf-8') as output_file:
    output_file.write('\n'.join(chat_messages))

print("Cleaned chat messages saved to 'cleaned_chat.txt'.")
