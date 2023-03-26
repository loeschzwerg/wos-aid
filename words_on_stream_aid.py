from sys import argv
from time import sleep
from itertools import permutations
from string import ascii_lowercase

from nltk.corpus import words, wordnet
import nltk
nltk.download('words')
nltk.download('wordnet')

words_ = set(words.words())

MINIMUM_WORD_LENGTH = 4
MINIMUM_CHAR_POOL_LENGTH = 6

def print_correct(w, syn, certainty):
  if syn:
    print(" " * (2 - certainty), "!" * certainty, w, "=", syn[0].definition())

def handle_input(word: str) -> str:
  """Handle interactive input. This input has four options: (-|+|!|q)"""
  choice = input("""
  [-<letter>] FAKE LETTER: remove a letter
  [+<letter>] MYSTERY LETTER: replace or add a letter
  [!<new-word>] NEW WORD: change the word to work on
  [q] quit
  > """)
  if '-' in choice and len(choice) == 2 and choice[1] in ascii_lowercase:
    return word.replace(choice[1], '', 1)
  elif '+' in choice and len(choice) == 2 and choice[1] in ascii_lowercase:
    if '?' in word:
      return word.replace('?', choice[1])
    else:
      return word + choice[1]
  elif '!' in choice and len(choice) > MINIMUM_CHAR_POOL_LENGTH:
    return choice[1:].lower()
  elif 'q' in choice and len(choice) == 1:
    exit(0)
  else:
    print("ERROR: Input not recognized")
    return handle_input(word)

def check_permutations(word: str):
  for cnt in range(MINIMUM_WORD_LENGTH, len(word) + 1):
    print(f"--- {cnt} letters ---")
    perms = {"".join(x) for x in set(permutations(word, cnt))}
    for w in sorted(perms):
      if '?' in w:
        for c in ascii_lowercase:
          rep = w.replace("?", c)
          syn = wordnet.synsets(rep)
          print_correct(rep, syn, 0)
      else:
        syn = wordnet.synsets(w)
        print_correct(w, syn, 2 if w in words_ else 1)

if __name__=="__main__":

  word = ""
  try: # take input from command-line
    word = argv[1]
  except: # take input from handle_input
    word = handle_input(word)

  while True:
    print("##### NEW WORD", "".join(sorted(word)), "#####") 
    check_permutations(word)
    word = handle_input(word)