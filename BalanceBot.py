# pip install chatterbot==1.0.4
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#from turtle import color
#from matplotlib.ft2font import BOLD
import tkinter as tk
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
print(training_list)
for pair in training_list:
    trainer.train(pair)

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
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
        y_list_resource_index = [index for (index, item) in enumerate(X_list) if item == "if beyond the data's comprehension."]
        response = str(y_list[y_list_resource_index[0]])
    else:
        for word in keywords:
            response = response + ' ' + str(chatbot.get_response(word))
    print(response)

## GUI FUNCTIONS ##
def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    return canvas1.create_polygon(points, **kwargs, smooth=True)


# GUI
# Initialize GUI
root = tk.Tk()
canvas1 = tk.Canvas(root, width=600, height=300)
root.resizable(False, False)
canvas1.pack()
# Size and background color of output GUI
background = tk.PhotoImage(file=botbackground)
background = background.subsample(1, 1)
canvas1.create_image(300, 200, image=background)
# Round edges of output GUI
rect = round_rectangle(100, 105, 500, 225, fill="#d9a5b1")
# Add title to output GUI
root.title("BalanceBot")
#titleArt=tk.PhotoImage(file=wordArt_address)
#titleArt=titleArt.subsample(2,2)
#canvas1.create_image(300, 55, image = titleArt)
# Create entry box to collect input joke
canvas1.create_text(300, 130, fill="white", font=('futura', 22), text='Start chat with BalanceBot. ')
entry1 = tk.Entry(root, bd=0) # create 1st entry box
canvas1.create_window(300, 160, width=350, window=entry1)
# Button
#button = tk.Button(root, font=('futura'), text='Enter', bd=0, command=values)
#canvas1.create_window(300, 200, window=button)
root.mainloop()