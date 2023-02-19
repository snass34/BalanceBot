# pip install chatterbot==1.0.4
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

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