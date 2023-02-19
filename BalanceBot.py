# pip install chatterbot==1.0.4
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pandas as pd
import string
import os

## OPEN NECESSARY FILES
# Path to prev dir contains this file
dir = os.path.abspath(os.path.dirname(__file__))
# -> open data file with this directory
data_file_address = os.path.join(dir, "DataTrainChatBot.csv")
botbackground = os.path.join(dir, "Pictures/botbackground.png")

## READ AND DEFINE DATA VARIABLES
df = pd.read_csv(data_file_address)
# Independent variables
X = df['Word']
# Dependent variable
y = df['Potential Response']

X_list = X.values.tolist()
y_list = y.values.tolist()

# Convert lists to lowercase
for i in range(len(X_list)):
    X_list[i] = (str(X_list[i])).lower()
    X_list[i] = (str(X_list[i])).strip()
for i in range(len(y_list)):
    y_list[i] = (str(y_list[i])).strip()

chatbot = ChatBot('BalanceBot')
trainer = ListTrainer(chatbot)

training_list = []
for i in range(len(X_list)):
    pair = [X_list[i], y_list[i]]
    training_list.append(pair)
for pair in training_list:
    trainer.train(pair)

def handle_query(query):
    exit_conditions = (":q", "quit", "exit")
    while True:
        #query = input("> ")
        query = query.lower()
        # Remove punctuation from input
        query = query.translate(str.maketrans('', '', string.punctuation))
        # Log which words are in database
        input_word_list = query.split()
        keywords = []
        for item in input_word_list:
            if item in X_list:
                keywords.append(item)
        # remove repeated occurrences of keywords
        keywords = list(set(keywords))
        response = ""
        if query in exit_conditions:
            break
        elif len(keywords) == 0:
            y_list_resource_index = [index for (index, item) in enumerate(X_list) if
                                     item == "if beyond the data's comprehension."]
            response = str(y_list[y_list_resource_index[0]])
        else:
            for word in keywords:
                response = response + ' ' + str(chatbot.get_response(word))
        return response


## GUI FUNCTIONS ##
# Send function
def send():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)
    query = str(e.get().lower())
    response = handle_query(query)
    txt.insert(END, "\n" + "Bot -> "+str(response))
    e.delete(0, END)

# GUI
def center_window(width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

root = Tk()
root.geometry("530x470")
root.title("BalanceBot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=65, wrap=WORD)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=send).grid(row=2, column=1)
root.mainloop()