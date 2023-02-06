from tkinter import *
import tkinter
import random


# Setup Tkinter
root = Tk()
root.title("Disappearing Text Writing App")
root.geometry('800x600')
frame = tkinter.Frame(root)
root.configure(bg='#DFD3C3')

# Setup fonts
root.option_add('*Label.font', 'Helvetica 20')
root.option_add('*Label.font', 'Helvetica 20')



# Title Label
title_label = Label(root, text="Disappearing Text Writing App", bg='#DFD3C3')
title_label.place(relx=0.5, rely=0.1, anchor=CENTER)

# Instructions Labels
instructions_label = Label(root, text='The text you typed will disappear 5 seconds after you stop typing.\n'
                                      'You can generate random words by clicking the "RANDOM WORDS" button below', bg='#DFD3C3')
instructions_label.place(relx=0.5, rely=0.2, anchor=CENTER)



# User Entry Box
user_entry = Text(root, height=7, width=50, bg='#F8EDE3', fg='black')
user_entry.place(relx=0.5, rely=0.5, anchor=CENTER)
entry = ""
count = 0


def generate_random_words():
    global user_entry
    with open("textfile.txt", "r") as possible_texts:
        lines = possible_texts.readlines()
        random_words = random.choice(lines).split(" ")
        words = random.choices(random_words, k=8)
        line = ' '.join(words)
        user_entry.focus_set()
        user_entry.delete(1.0, "end-1c")
        user_entry.insert("end-1c", line)


#  Button to Generate Random Words
random_words_button = Button(root, text="RANDOM WORDS", bg='#F8EDE3', fg='black', command=generate_random_words, relief=RAISED)
random_words_button.place(relx=0.5, rely=0.7, anchor=CENTER)



def remove_text():
    user_entry.delete(1.0, tkinter.END)
    user_entry.insert(tkinter.END, "")

def disappear_text():
    global count, entry
    if entry == user_entry.get(1.0, tkinter.END):
        if count == 5:
            root.after(1000, remove_text)
            count = -1
        root.after(1000, disappear_text)
        count += 1
    else:
        root.after(3000, disappear_text)
        entry = user_entry.get(1.0, tkinter.END)
        count = 0

root.after(1000, disappear_text)
root.mainloop()