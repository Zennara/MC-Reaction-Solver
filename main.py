import time
import os
import pyautogui
import random

log_file_path = os.getenv("APPDATA") + "/.minecraft/logs/latest.log"

# switch to minecraft window automatically
SWITCH_WINDOW = True
LOG_UNSCRAMBLES = True

# disable failsafe (allow mouse movement)
pyautogui.FAILSAFE = False


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

                # detections
                if "Reaction » " in chat_message:
                    after_reaction = chat_message.split("Reaction » ", 1)[1]

                    # Reaction » Unscramble the word estt for a random prize!
                    if after_reaction.startswith("Unscramble"):
                        pass

                    # log unscramble words
                    if LOG_UNSCRAMBLES:
                        start_string = " unscrambled the word "
                        end_string = " in "

                        start_index = after_reaction.find(start_string) + len(start_string)
                        end_index = after_reaction.find(end_string)

                        if start_index != -1 and end_index != -1:
                            logged_word = after_reaction[start_index:end_index]
                            if not os.path.isfile('unscrambles.txt'):
                                # Create the file if it doesn't exist
                                open('unscrambles.txt', 'a').close()

                            # Read the contents of the text file
                            with open('unscrambles.txt', 'r') as file:
                                lines = file.readlines()

                            # Check if the word exists in the file
                            if logged_word + '\n' not in lines:
                                # Append the word to a new line in the file
                                with open('unscrambles.txt', 'a') as file:
                                    file.write(logged_word + '\n')

                                print(f"The word '{logged_word}' was added to the file.")
                            else:
                                print(f"The word '{logged_word}' already exists in the file.")

                    # Reaction » Type the word TEST for a random prize!
                    if after_reaction.startswith("Type"):
                        start_string = "Type the word "
                        end_string = " for a random prize!"

                        start_index = after_reaction.find(start_string) + len(start_string)
                        end_index = after_reaction.find(end_string)

                        if start_index != -1 and end_index != -1:
                            desired_word = after_reaction[start_index:end_index]
                            type_macro(desired_word)

                    # Reaction » Solve the expression 100 - 50 for a random prize!
                    if after_reaction.startswith("Solve"):
                        start_string = "Solve the expression "
                        end_string = " for a random prize!"

                        start_index = after_reaction.find(start_string) + len(start_string)
                        end_index = after_reaction.find(end_string)

                        if start_index != -1 and end_index != -1:
                            expression = after_reaction[start_index:end_index]
                            expression = expression.replace('x', '*')
                            result = eval(expression)
                            type_macro(str(result))


def type_macro(text):
    # Generate a random delay between 1 and 1.5 seconds
    delay = random.uniform(1, 1.5)

    # Sleep for the random delay
    time.sleep(delay)

    if SWITCH_WINDOW:
        # Find the Minecraft window by its title
        minecraft_windows = [window for window in pyautogui.getAllTitles() if window.startswith('Minecraft')]

        if minecraft_windows:
            # Activate the first Minecraft window found
            minecraft_window = pyautogui.getWindowsWithTitle(minecraft_windows[0])[0]
            minecraft_window.maximize()
            minecraft_window.activate()
        else:
            print("Minecraft window not found")

    # Type the answer
    pyautogui.press('t')
    pyautogui.typewrite(text)
    pyautogui.press('enter')

    line = "-" * 30
    print(f"{line}\nSolved: {text} in {delay}\n{line}")


# Call the function to start reading the chat log
read_chat_log()
