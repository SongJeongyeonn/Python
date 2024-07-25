import keyboard
import turtle as t
t.shape('turtle')
while True:
    if keyboard.is_pressed('up'):
        t.forward(5)
    if keyboard.is_pressed('down'):
        t.backward(5)
    if keyboard.is_pressed('left'):
        t.left(10)
    if keyboard.is_pressed('right'):
        t.right(10)
    if keyboard.is_pressed('a'):
        print("quit")
        quit()
        break