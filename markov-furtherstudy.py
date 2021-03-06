"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    full_string = str()
    f = open(file_path)
    full_string = f.read()
    
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    return full_string


def make_chains(text_string, n=2):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    

    # your code goes here
    text_list = text_string.split()
    chains = {}

    for i in range(len(text_list)-n):
        key = tuple(text_list[i:i+n])
        value = text_list[i+n]
        chains[key] = chains.get(key,[]) + [value]

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    new_key = choice(list(chains.keys()))
    n = len(new_key)
    
    while new_key[0] != new_key[0].title():
        new_key = choice(list(chains.keys()))

    for i in range(n):
        words.append(new_key[i])

    while new_key in chains:
        new_keys_value = choice(chains[new_key])

        words.append(new_keys_value)

        new_key = new_key[1:] + tuple([new_keys_value])

        #break if the last character is a punctuation

        if new_key[-1:][-1].isalpha() == False:
            break

    # your code goes here

    return " ".join(words)



input_path = sys.argv[1]
n = int(sys.argv[2])

input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text,n)

# Produce random text
random_text = make_text(chains)

print(random_text)
