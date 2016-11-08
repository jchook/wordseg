import re
from itertools import groupby
import os

cleanup = re.compile(r'[^a-z0-9]')

# http://stackoverflow.com/a/481773/554406
def segment(text):
  text = re.sub(cleanup, '', text)
  probs, lasts = [1.0], [0]
  for i in range(1, len(text) + 1):
    prob_k, k = max(
      (probs[j] * word_prob(text[j:i]), j)
      for j in range(max(0, i - max_word_length), i)
    )
    probs.append(prob_k)
    lasts.append(k)
  words = []
  i = len(text)
  while 0 < i:
    words.append(text[lasts[i]:i])
    i = lasts[i]
  words.reverse()
  return words, probs[-1]

def word_prob(word): return dictionary.get(word, 0) / total

def entry(line): 
  w, c = line.split("\t", 2)
  return (w, int(c))

dict_path = os.path.join(os.path.dirname(__file__), 'dict.txt')
dictionary = dict(entry(line) for line in open(dict_path))
max_word_length = max(map(len, dictionary))
total = float(sum(dictionary.values()))