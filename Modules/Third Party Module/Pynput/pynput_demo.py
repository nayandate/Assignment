# from pynput import keyboard
# def press(key):
#     print("Key pressed:", key)
# def release(key):
#     print("Key released:", key)
# listener = keyboard.Listener(on_release=release,on_press=press)
# listener.start()
# listener.join()



from pynput.keyboard import Controller
keyboard = Controller()
keyboard.press("a")
keyboard.release("a")
keyboard.type("HELLO Nayan")


# from pynput.keyboard import Controller, Key
# keyboard = Controller()
# keyboard.type("Hello World")
# keyboard.type("This is Pynput")



