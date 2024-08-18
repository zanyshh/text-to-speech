import tkinter
import customtkinter as tk
import pyttsx3


def speak():
    text = text_entry.get()
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()



app = tk.CTk()
app.title('Text-to-Speech')
app.geometry('400x300')
app.iconbitmap('text-to-speech/resources/text-to-voice.ico')


text_entry = tk.CTkEntry(app,width=300,height=100,justify=tk.CENTER,placeholder_text='type here to convert into speech')
text_entry.pack(pady=10,padx=10)

speak_button = tk.CTkButton(app,text='speak',command=speak,fg_color='#a2d2ff',width=10,height=10)
speak_button.pack(pady=10)

app.mainloop()

