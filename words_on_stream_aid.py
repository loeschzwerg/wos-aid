from sys import argv
from time import sleep, time
from itertools import permutations
from string import ascii_lowercase

from nltk.corpus import words, wordnet
from nltk import download
download('words')
download('wordnet')
del download

# O(1) lookup
words_set = set(words.words())

### start handling words

MINIMUM_WORD_LENGTH = 4
MINIMUM_CHAR_POOL_LENGTH = 5


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
    sleep(1) # let the user read the message
    return handle_input(word)

def print_correct(w, syn, certainty):
  print(" " * (2 - certainty), "!" * certainty, w, "=", syn[0].definition())

def check_permutations(word: str):
  # t0, t1, t2, t3, t4 = time(), time(), time(), time(), time() # start, start #1, step #1, start #2, step #2
  for cnt in range(MINIMUM_WORD_LENGTH, len(word) + 1):
    print(f"--- {cnt} letters ---")
    # t1 = time()
    perms = {"".join(x) for x in set(permutations(word, cnt))}
    # t2 = time()
    # print("Permutations={:.2f}s | total={:.2f}s".format(t2-t1, t2-t0))
    for w in sorted(perms):
      # t3 = time()
      if '?' in w:
        for c in ascii_lowercase:
          rep = w.replace("?", c)
          syn = wordnet.synsets(rep)
          if syn:
            print_correct(rep, syn, 0)
      else:
        syn = wordnet.synsets(w)
        if syn:
          print_correct(w, syn, 2 if w in words_set else 1)
      # t4 = time()
    # t2 = time()
    # print("step={:.2f}s | total={:.2f}s".format(t2-t1, t2-t0))
  # print(f"last step={t4-t3:.4f} | last range={t4-t1:.4f} | total={t4-t0:.4f}")

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