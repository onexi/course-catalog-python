#  count words
# ---------------
import json    

def store_json(data,file):
    # Enter your code here

with open('titles_clean.json', 'r') as file:
    # Enter your code here - load json

    # remove punctuation/numbers
    # Enter your code here

    # count words
    # Enter your code here

    store_json(counts, 'visualization/word_count.js')
