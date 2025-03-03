import tkinter as tk
import pyttsx3

def speaknow():
    engine = pyttsx3.init()
    engine.say(text_v.get())
    engine.runAndWait()

root = tk.Tk()

text_v = tk.StringVar()

obj = tk.LabelFrame(root, text="Text to Speech", font=("Arial", 20), bd=1)
obj.pack(fill="both", expand=True, padx=10, pady=10)

lbl = tk.Label(obj, text="Text:", font=("Arial", 15))
lbl.grid(row=0, column=0, padx=5, pady=5)

text = tk.Entry(obj, textvariable=text_v, font=("Arial", 15), width=25, bd=5)
text.grid(row=0, column=1, padx=10, pady=5)

btn = tk.Button(obj, text="Speak", font=("Arial", 15), bg="black", fg="white", command=speaknow)
btn.grid(row=0, column=2, padx=10, pady=5)

root.title("Text to Speech")
root.geometry("500x100")
root.resizable(False, False)
root.mainloop()
