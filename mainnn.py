import re

# Open the file containing the tweets
with open('tweets.txt', 'r') as file:

    # Read the tweets into a list
    tweets = file.readlines()

# Open the file containing the racial slurs
with open('slurs.txt', 'r') as file:

    # Read the racial slurs into a set
    racialSlurs = set(file.read().split())

# Define a function to calculate the degree of profanity for each tweet
def calculate_profanity(tweet):

    # Use regular expressions to split the tweet into words
    words = re.findall(r'\w+', tweet.lower())

    # Count the number of racial slurs in the tweet
    num_racial_slurs = len(racialSlurs.intersection(words))

    # Calculate the degree of profanity for the tweet
    if num_racial_slurs == 0:
        return "Not profane"
    elif num_racial_slurs == 1:
        return "Slightly profane"
    elif num_racial_slurs == 2:
        return "Moderately profane"
    else:
        return "Highly profane"

# Calculate the degree of profanity for each tweet and print the results
for tweet in tweets:
    degree_of_profanity = calculate_profanity(tweet)
    print(f"{tweet.strip()} :: {degree_of_profanity}")
