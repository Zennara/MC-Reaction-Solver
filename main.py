import time
import os

log_file_path = os.getenv("APPDATA") + "/.minecraft/logs/latest.log"


def read_chat_log():
    with open(log_file_path, 'r') as log_file:
        log_file.seek(0, 2)  # Move the file pointer to the end of the file
        while True:
            new_line = log_file.readline()
            if not new_line:
                time.sleep(0.1)  # Wait for new content to be added to the file
                continue
            if '[CHAT]' in new_line:
                chat_message = new_line.split('[CHAT]')[1].strip()
                print(chat_message)


# Call the function to start reading the chat log
read_chat_log()
