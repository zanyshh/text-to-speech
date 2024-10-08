import tkinter
import customtkinter as tk
import pyttsx3


# funtion fot the speak button
def speak():
    text = text_entry.get()
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def rate():
    pass



# app window config
app = tk.CTk()
app.title('Text-to-Speech')
app.geometry('400x300')
app.iconbitmap('text-to-speech/resources/text-to-speech.ico')

# Window Frame
frame = tk.CTkFrame(app)
frame.pack(padx=10,pady=10)

# Entry label on window
text_entry = tk.CTkEntry(frame,
             width=300,
             height=100,
             justify=tk.CENTER,
             placeholder_text='type here to convert into speech')
text_entry.pack(pady=10,padx=10)

# Speak label on window
speak_button = tk.CTkButton(frame,
                           text='speak',
                           command=speak,
                           fg_color=('#00afb9'),
                           hover_color=('#005f73'),
                           width=100,
                           height=40)
speak_button.pack(pady=20)

# Slider to adjust speed of voice
#slider_button = tk.CTkSlider(frame,
#                             from_=0,to=100,
 #                            orient=tk.HORIZONTAL,
#                             command=rate)
# slider_button.pack(padx=10,pady=10)


if __name__ == '__main__':
   app.mainloop()

