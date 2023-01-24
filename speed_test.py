from tkinter import *
import random
from tkinter import messagebox


class Speed_Test:

    def __init__(self):
        # setting window
        self.window = Tk()
        self.window.title("Typing Speed Test")
        self.window.minsize(width=1000, height=500)
        self.window.config(padx=20, pady=20)


        # variables
        self.text_list = []
        self.typed_text = ''


        # setting text to be typed
        self.text = Text(self.window, height=10, width=50, wrap=WORD)
        self.text.config(font=60)

        self.text.insert(END, ' '.join(self.generate_text()))
        self.text.tag_configure('center', justify='center')
        self.text.tag_add('center', "1.0", "end")
        self.text.place(x=500, y=25, anchor='n')

        # setting where the user will type
        self.entry = Entry(width=25, justify='center')
        self.entry.insert(END, string="")
        self.entry.config(font=60)
        self.entry.place(x=500, y=350, anchor='center')


        # countdown
        self.label = Label(self.window, text="", width=10)
        self.label.place(x=100, y=200)
        self.remaining = 0
        self.countdown(60)


        self.window.bind("<space>", self.check_word)
        self.window.mainloop()

    def generate_text(self):
        # generating random text
        with open(file="english_words.txt") as all_words_txt:
            all_words = all_words_txt.readlines()
            self.text_list = []
            for word in range(0, 200):
                self.text_list.append(all_words[random.randint(0, len(all_words))].rstrip())
        return self.text_list

    def check_word(self, button_press):
        sample_text_list = self.text_list
        word = self.entry.get()
        self.typed_text += word
        self.typed_text_list = self.typed_text.split()
        self.entry.delete(0, 'end')
        # for N in range(0, len(self.typed_text_list)):
        #     if self.typed_text_list[N] == sample_text_list[N]:
        #         self.text.tag_add('right', )

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="time's up!")
            self.results()
        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.window.after(1000, self.countdown)

    def results(self):
        right = 0
        wrong = 0
        for N in range(0, len(self.typed_text_list)):
            if self.typed_text_list[N] == self.text_list[N]:
                right += 1
            else:
                wrong += 1
        acc = (right/(right+wrong))*100
        messagebox.showinfo('RESULTS', message=f"Your WPM is {len(self.typed_text_list)} with {acc}% of accuracy")




