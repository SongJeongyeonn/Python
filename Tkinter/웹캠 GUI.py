import cv2
import torch
import tkinter as tk
from PIL import Image, ImageTk

def update_frame():
    button.config(text="실행 중")
    ret, frame = cap.read()
    if ret:
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = model(img_rgb)
        frame = results.render()[0]
        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        img_tk = ImageTk.PhotoImage(image=img)
        label.img_tk = img_tk
        label.config(image=img_tk)
    root.after(10, update_frame)
from tkinter import font
def camera_detection():
    top = tk.Toplevel(root)
    top.title("카메라 설명서")

    explanation_text = (
        "위험 물건 탐지 카메라 설명서\n\n"
        "1. '카메라 실행' 버튼을 클릭하여 카메라를 실행합니다.\n"
        "2. 카메라가 화면에 있는 물체를 감지하여 어떤 물체인지 표시합니다.\n"
        "3. '카메라 설명서' 버튼을 클릭하여 이 창을 다시 열 수 있습니다.\n"
        "4. 프로그램을 종료하려면 창을 닫으면 됩니다.\n\n"
    )

    custom_font = font.Font(family="Helvetica", size=14, weight="bold")
    label = tk.Label(top, text=explanation_text, padx=20, pady=20, wraplength=400, font=custom_font, fg="black", bg="white")
    label.pack()
    
    close_button = tk.Button(top, text="닫기", command=top.destroy)
    close_button.pack(pady=10)

root = tk.Tk()
root.title("위험 물건 탐지 카메라")

icon_image = Image.open('0.png')
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(True, icon_photo)

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    root.destroy()
    exit()

label = tk.Label(root)
label.pack()

button = tk.Button(root, text='카메라 실행',bg='gray77',font=17,width=20,height=3, command=update_frame)
button2 = tk.Button(root, text='카메라 설명서',bg='ivory4',font=17,width=20,height=3, command=camera_detection)
button.pack(side=tk.LEFT, padx=10, pady=10)
button2.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()

cap.release()
cv2.destroyAllWindows()