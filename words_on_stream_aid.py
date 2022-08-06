from sys import argv

from itertools import permutations
from string import ascii_lowercase
from nltk.corpus import words, wordnet
# nltk.download('words')
# nltk.download('wordnet')

if argv[1]:
  word = argv[1]
else:
  print("Give input, LUL")
print("##### NEW WORD", "".join(sorted(word)), "#####")

words_ = set(words.words())

def print_correct(w, syn, certainty):
  if syn:
    print(" "*(2-certainty), "!"*certainty, w, "=", syn[0].definition())

for cnt in range(4, len(word)+1):
  print(f"--- {cnt} letters ---")
  perms = {"".join(x) for x in set(permutations(word, cnt))}
  for w in sorted(perms):
    if '?' in w:
      for c in ascii_lowercase:
        rep = w.replace("?",c )
        syn = wordnet.synsets(rep)
        print_correct(rep, syn, 0)
    else:
      syn = wordnet.synsets(w)
      print_correct(w, syn, 2 if w in words_ else 1)
