import tkinter as tk
from gtts import gTTS
import playsound
import os

def speaknow():
    text = text_v.get()  # รับข้อความจากช่องกรอก
    if text.strip():  # ตรวจสอบว่าไม่ใช่ข้อความว่าง
        tts = gTTS(text=text, lang="th")  # สร้างเสียงภาษาไทย
        filename = "voice.mp3"
        tts.save(filename)  # บันทึกเป็นไฟล์ MP3
        playsound.playsound(filename)  # เล่นเสียง
        os.remove(filename)  # ลบไฟล์หลังจากเล่นเสร็จ

root = tk.Tk()

text_v = tk.StringVar()

obj = tk.LabelFrame(root, text="Text to Speech (Thai)", font=("Arial", 20), bd=1)
obj.pack(fill="both", expand=True, padx=10, pady=10)

lbl = tk.Label(obj, text="ใส่ข้อความ:", font=("Arial", 15))
lbl.pack(side=tk.LEFT, padx=5)

text = tk.Entry(obj, textvariable=text_v, font=("Arial", 15), width=25, bd=5)
text.pack(side=tk.LEFT, padx=10)

btn = tk.Button(obj, text="อ่านออกเสียง", font=("Arial", 15), bg="black", fg="white", command=speaknow)
btn.pack(side=tk.RIGHT, padx=10)



root.title("Text to Speech (Thai)")
root.geometry("600x200")
root.resizable(False, False)
root.mainloop()
