# wos-aid
A little python script that will aid in achieving all your `words on stream` goals

## Install
Install nltk
```bash
pip3 install --user nltk 
```
Ready to go!

## Run
```bash
# garbled word is optional
python3 -m words_on_stream_aid
python3 -m words_on_stream_aid <garbled_word>
```

## Example
```bash
$ python3 -m words_on_stream_aid word
  [-<letter>] FAKE LETTER: remove a letter
  [+<letter>] MYSTERY LETTER: replace or add a letter
  [!<new-word>] NEW WORD: change the word to work on
  [q] quit
  > !buffalo
##### NEW WORD abfflou #####
--- 4 letters ---
 !! bola = a cord fastened around the neck with an ornamental clasp and worn as a necktie
 !! buff = an ardent follower and admirer
 !! bufo = any toad of the genus Bufo
  ! flab = loose or flaccid body fat
 !! flub = an embarrassing mistake
 !! foal = a young horse
 !! foul = an act that violates the rules of a sport
  ! fula = a member of a pastoral and nomadic people of western Africa; they are traditionally cattle herders of Muslim faith
 !! loaf = a shaped mass of baked bread that is usually sliced before eating
  ! luba = a member of a Bantu people in southeastern Congo
 !! luff = (nautical) the forward edge of a fore-and-aft sail that is next to the mast
--- 5 letters ---
 !! afoul = especially of a ship's lines etc
 !! bluff = a high steep bank (usually formed by river erosion)
  ! luffa = the dried fibrous part of the fruit of a plant of the genus Luffa; used as a washing sponge or strainer
 !! offal = viscera and trimmings of a butchered animal often considered inedible by humans
--- 6 letters ---
--- 7 letters ---
 !! buffalo = large shaggy-haired brown bison of North American plains

  [-<letter>] FAKE LETTER: remove a letter
  [+<letter>] MYSTERY LETTER: replace or add a letter
  [!<new-word>] NEW WORD: change the word to work on
  [q] quit
```