#this reads the text file from text_read being a txt fiel:
import urllib.request  
import string
import json

target_url = 'https://www.gutenberg.org/cache/epub/67709/pg67709.txt'




f = urllib.request.urlopen(target_url)
data = f.read().decode('utf-8')








def process_file(filemane, skip_header):
    """this takes the file given in url form and opens the url and proceeds to read it"""
    hist = {}


    if skip_header:
        skip_gutenberg_header(data)

    strippables = string.punctuation + string.whitespace

    for line in data:
        if line.startswith('*** END OF THE PROJECT'):
            break

        line = line.replace('-', ' ')


        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()

            hist[word] = hist.get(word, 0) + 1

    return hist




    


    





def skip_gutenberg_header(data):
    """This function find the start of the project text found in gutenberg files in which it skips the introductionary writing and gets to the text."""
    for line in data:
        if line.startswith('*** START OF THE PROJECT'):
            break




def total_letter(hist):
    """this adds up the amount of letters stored in hist and adds up the total amount to give out the total sum of all letters calculated"""
    return sum(hist.values())



    
def random_letter(hist):
    """this function randomly goes through the text and chooses a random number and chooses a letter from the selection within the text file given"""
    import random
    t = []
    for word, freq in hist.items():
        t.extend([word] * freq)

    return random.choice(t)

def most_common_letters(hist, excluding_stopwords=False):
    """this function counts the amount of times each letter shows up and sorts them in order from highest to lowest"""
    letters = []
    for word, freq in hist.items():
        letters.append((freq,word))
    letters.sort(reverse=True)
    return letters



___main___ = '___main___'
print(data)
print(process_file(data, skip_header=True))
hist = process_file(data, skip_header=True)
print(total_letter(hist))
print(random_letter(hist))
print(most_common_letters(hist,excluding_stopwords=False))















