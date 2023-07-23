# KeyLogger
•This Python code implements a basic keylogger using the 'pynput' library to capture keyboard input events on a Windows system. It records the key presses, holds, and releases and saves them in two files: a text file ('log4.txt') and a JSON file ('logs4.json'). Let's go through the code step by step:

1.Importing Required Modules:

• 'pynput.keyboard': This module is used for monitoring and controlling keyboard input.
• 'json': This module is used for reading and writing JSON data.
• 'datetime': This module provides functions to work with dates and times.
• 'ctypes': This module allows calling functions from shared libraries (DLLs) in Windows.

2.Function Definitions:
• 'get_caps_lock_state()': This function uses the 'ctypes' library to get the state of the Caps Lock key. It returns 'True' if the Caps Lock is active and 'False' if it's inactive.
• 'update_txt_file(key)': This function is responsible for updating the text file ('log4.txt') with the captured keystrokes. It handles special keys such as space, enter, escape, backspace, and caps lock, and records the key presses, accounting for the caps lock state.
• 'update_json_file(key_list)': This function updates the JSON file ('logs4.json') with the captured keystrokes in a structured format. It includes a timestamp indicating when the log was updated and the list of key events captured during the session.
• 'on_press(key)': This function is a callback function that is triggered when a key is pressed. It appends the pressed key to the 'key_list' list, distinguishing between normal press and hold events. If the 'ESC' key is pressed, it updates the JSON file and terminates the keylogger.
• 'on_release(key)': This function is a callback function that is triggered when a key is released. It appends the released key to the 'key_list' list. If the 'ESC' key is released, it updates the JSON file and terminates the keylogger. Additionally, if the 'Backspace' key is released, the last character in the text file is removed. Otherwise, it updates the text file with the captured key.
• 'save_logs()': This function is called at the beginning of the script to update the text file with a timestamp indicating when the keylogger was started.
• 'new_line()': This function adds a new line to the text file.

3.Main Execution:
• The script starts by calling the 'save_logs()' function to update the 'log4.txt' file with a timestamp indicating when the keylogger was started.
• It then initiates the keyboard listener using 'keyboard.Listener'. The 'on_press' and 'on_release' callback functions are provided to handle keyboard events.
• While the listener is active, it captures the key presses, holds, and releases. The key events are recorded in the 'key_list' list, and the text file ('log4.txt') is updated in real-time.
• Pressing the 'ESC' key triggers the termination of the keylogger. At this point, the captured keystrokes are saved to the JSON file ('logs4.json') using the 'update_json_file(key_list)' function.
