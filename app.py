from tkinter import *
from chat import get_response, bot_name
import time
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

BG_GRAY = "#302b54"
BG_COLOR = "#8884b0"
TEXT_COLOR = "#000000"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def mic(self):
        print('Initializing.....')
        listener = sr.Recognizer()  # Intializing Recognizer
        engine = pyttsx3.init()  # Initializing text to speech
        voices = engine.getProperty('voices')  # Changing voice of Assistant 0 or 1
        engine.setProperty('voice', voices[0].id)
        engine.setProperty("rate", 130)  # speed of text to speech

        def speak(info):
            engine.say(info)
            engine.runAndWait()


        def internal_execute():
            try:
                with sr.Microphone() as source:
                    print("Listening....")
                    speak("Listening....")
                    voice = listener.listen(source)
                    action = listener.recognize_google(voice)
                    action = action.lower()
                    if 'Casper' in action.lower():  # Hotword Detection
                        action = action.replace('Casper', '')
                        print(action)
                        # return action
                    else:
                        pass
            except:
                result_run()
            return action

        def result_run():  # conditions to Casper(bot) play,search,etc....
            command = internal_execute()
            print(command)
            if 'play' in command:
                term = command.replace('play', '')
                print('Playing' + term)
                speak('playing' + term)
                pywhatkit.playonyt(term)
                time.sleep(7)
            elif 'time' in command:
                timeis = datetime.datetime.now().strftime('%I:%M %p')
                print('Current Time is ' + timeis)
                speak('Current Time is ' + timeis)
            elif 'tatkal' and 'when' in command:
                speak(
                    'Tatkal booking opens for the selected trains at 10:00 am for AC classes and for non-AC classes at 11:00 am , one day in advance of the date of journey')
            elif 'how' and 'complaint' in command:
                speak(
                    'You can contact our customer care number at 011-39340000 or you can reach us through mail at  care@irctc.co.in')
            elif 'refund' and 'tatkal' in command:
                speak('No refund will be granted on cancellation of confirmed Tatkal tickets')
            elif 'pnr' and 'status' in command:
                speak('You can check the status of your ticket in the below website')
                print('http://www.indianrail.gov.in/enquiry/PNR/PnrEnquiry.html?locale=en')
            elif 'what is pnr' in command:
                speak(
                    'A passenger name record is a record in the database of a computer reservation system that contains the itinerary for a passenger or a group of passengers travelling together. ')
            elif 'refund' and 'general' in command:
                speak(
                    'For cancellation of unreserved, RAC and waitlisted tickets, the cancellation charges are Rs 30 for unreserved (second class) and Rs 60 for second class (reserved) and other classes')
            elif 'how to book' and 'ticket' in command:
                speak('Sure!')
                speak(
                    'Click on the log in option on the homepage After logging in, go to ‘Book Your Ticket’ page Enter starting and ending station, boarding and destination station. Select date of your journey and the class in which you want to travel. Check for the seat availability in the train of your choice. If seats are available, click on “book now” option. Add required details to book tickets. Enter mobile number and captcha. Then, pay charges online using credit card, debit card, net banking or UPI – whichever is convenient Finally, you will receive a message on your phone')
            elif 'what is' or 'whats' or 'what do you' or 'wikipedia' or 'who' in command:
                if 'what is' in command:
                    term = command.replace('what is', '')
                if 'whats' in command:
                    term = command.replace('whats', '')
                if 'what do you' in command:
                    term = command.replace('what do you', '')
                if 'wikipedia' in command:
                    term = command.replace('wikipedia', '')
                if 'who' in command:
                    term = command.replace('who', '')
                if 'what are' in command:
                    term = command.replace('what are', '')
                try:
                    value = wikipedia.summary(term, 1)
                    print(value)
                    speak(value)
                except:
                    speak('Sorry could not understand. Please repeat once again')
            else:
                speak('Could not Understand. Please repeat once again')
                result_run()

        speak("Hello sir, I am Casper, how can I help you today?")
        while True:
            result_run()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=700, height=900, bg=BG_COLOR)


        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#9d9bab", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.2)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=200, bg="#9bb396",
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.8, rely=0.008, relheight=0.06, relwidth=0.22)

        # Mic Button
        mic_button = Button(bottom_label, text="Mic", font=FONT_BOLD, width=200, bg="#9bb396",
                            command=lambda: self.mic())
        mic_button.place(relx=0.0, rely=0.008, relheight=0.06, relwidth=0.2)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
