import tkinter
import customtkinter as tk
import pyttsx3

# funtion fot the speak button
def speak():
    text = text_entry.get()
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# app window config
app = tk.CTk()
app.title('Text-to-Speech')
app.geometry('400x300')
app.iconbitmap('text-to-speech/resources/text-to-voice.ico')

# Entry label on window
text_entry = tk.CTkEntry(app,
             width=300,
             height=100,
             justify=tk.CENTER,
             placeholder_text='type here to convert into speech')
text_entry.pack(pady=10,padx=10)

# Speak label on window
speak_button = tk.CTkButton(app,
                           text='speak',
                           command=speak,
                           fg_color=('#00afb9'),
                           hover_color=('#005f73'),
                           width=100,
                           height=40)
speak_button.pack(pady=20)

app.mainloop()

