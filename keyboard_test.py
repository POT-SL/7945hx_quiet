from pynput import keyboard


def on_press(key):
    print(f'按键 {key} 被按下')


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

print(1)