import os
import pandas as pd
import string

## OPEN NECESSARY FILES
# Path to prev dir contains this file
dir = os.path.abspath(os.path.dirname(__file__))
# -> open data file with this directory
data_file_address = os.path.join(dir, "DataTrainChatBot.csv")
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

# Example input
input = "I am feeling sad today."
# Convert input to lowercase
input = input.lower()
# Remove punctuation from input
input = input.translate(str.maketrans('', '', string.punctuation))
# Log which words are in database
input_word_list = input.split()
print(input_word_list)
for word in input_word_list:
    if word in X_list:
        print('lkfsofijoidsjfoidj',word)

