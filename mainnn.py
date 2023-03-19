import re

with open('tweets.txt', 'r') as file:
    tweets = file.readlines()

with open('slurs.txt', 'r') as file:
    racialSlurs = set(file.read().split())

def calculate_profanity(tweet):
    words = re.findall(r'\w+', tweet.lower())
    num_racial_slurs = len(racialSlurs.intersection(words))
    if num_racial_slurs == 0:
        return "Not profane"
    elif num_racial_slurs == 1:
        return "Slightly profane"
    elif num_racial_slurs == 2:
        return "Moderately profane"
    else:
        return "Highly profane"

for tweet in tweets:
    degree_of_profanity = calculate_profanity(tweet)
    print(f"{tweet.strip()} :: {degree_of_profanity}")

#Steps involved:
## Open the file containing the tweets
## Read the tweets into a list
## Open the file containing the racial slurs
## Read the racial slurs into a set
## to calculate the degree of profanity for each tweet
## Use regular expressions to split the tweet into words
## Count the number of racial slurs in the tweet
## Calculate the degree of profanity for the tweet
## Calculate the degree of profanity for each tweet 