import time
import os
import pyautogui
import random
import re

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

                    # Reaction » Unscramble the word htasg for a random prize!
                    if after_reaction.startswith("Unscramble"):

                        def extract_string(text, start_string, end_string):
                            pattern = rf"{re.escape(start_string)}(.*?){re.escape(end_string)}"
                            match = re.search(pattern, text)
                            if match:
                                return match.group(1)
                            return None

                        def check_string_match(file_path, search_string):
                            with open(file_path, 'r') as file:
                                for line in file:
                                    line = line.strip()
                                    if sorted(search_string) == sorted(line) and len(search_string) == len(line):
                                        return line
                            return None

                        # Example usage
                        unscrambles_file = 'unscrambles.txt'
                        start_string = "Unscramble the word "
                        end_string = " for a random prize!"

                        # Extract the string between start and end strings from the provided string
                        extracted_string = extract_string(after_reaction, start_string, end_string)

                        if extracted_string:
                            print("Extracted string:", extracted_string)

                            # Check if the characters of the extracted string match any line in unscrambles file
                            matched_word = check_string_match(unscrambles_file, extracted_string)

                            if matched_word:
                                type_macro(matched_word, 1)
                            else:
                                print("No matching word found in the unscrambles file")
                        else:
                            print("No matching string found in the provided string")

                    # log unscramble words
                    if LOG_UNSCRAMBLES:
                        start_string = " unscrambled the word "
                        end_string = " in "

                        if start_string in after_reaction and end_string in after_reaction:
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
                            type_macro(desired_word, 2)

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
                            type_macro(str(result), 3)


def type_macro(text, type):

    # Generate a random delay between 1 and 1.5 seconds
    match type:
        case 1:
            # unscramble
            delay = random.uniform(1.25, 1.75)
        case 2:
            # type word
            delay = random.uniform(1, 1.5)
        case 3:
            # solve expression
            delay = random.uniform(1.5, 2)

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
