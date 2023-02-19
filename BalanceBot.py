# pip install chatterbot==1.0.4
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#from turtle import color
#from matplotlib.ft2font import BOLD
import tkinter as tk
import os

dir = os.path.abspath(os.path.dirname(__file__))
botbackground = os.path.join(dir, "Pictures/botbackground.png")

chatbot = ChatBot('BalanceBot')
trainer = ListTrainer(chatbot)
l = [["Hi", "Welcome, friend 🤗",],
     ["Hi", "bananas, friend",],
     ["Are you a plant?", "No, I'm the pot below the plant!"]]

for item in l:
    trainer.train(item)

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")

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