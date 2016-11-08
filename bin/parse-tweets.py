# -*- coding: utf-8 -*-
# Python 2 is dumb re: unicode

# Start with a file that has a one tweet JSON object per line (from the API).
# Outputs a file that has a simple space-separated list of words per line.

# Built-in
import sys
import json
import re
import argparse
import codecs

# Parse arguments
parser = argparse.ArgumentParser(description='Convert tweet JSON to a simple text file')
parser.add_argument('infile', nargs='?', type=lambda s: codecs.open(s, 'r', 'utf-8'), default=codecs.getreader('utf-8')(sys.stdin))
parser.add_argument('outfile', nargs='?', type=lambda s: codecs.open(s, 'w', 'utf-8'), default=codecs.getreader('utf-8')(sys.stdout))
args = parser.parse_args()

ignoreChars = set(["'"])
wordBreakChars = set([' ', '-'])
specialPrefixes = set(['@','#','&'])
spaceSaver = re.compile(ur' {2,}')

def is_allowed_char(ustr):
  return is_alphanumeric(ustr)

def is_alphanumeric(ustr):
  if (ustr < '0') or (ustr > 'z'):
    return False
  return not (
    (ustr > '9' and ustr < 'A') or
    (ustr > 'Z' and ustr < 'a')
  )

def clean_tweet(tweet):

  # Clean hashtags, @username, hyperlinks, and html entities
  clean = ''
  for word in tweet.split():
    if len(word) == 0:
      continue
    if word[0] in specialPrefixes:
      continue
    if word[:4] == 'http':
      continue
    clean += (word + ' ')

  # Clean unwanted chars and punctuation
  hyperclean = ''
  for char in clean:
    if is_allowed_char(char):
      hyperclean += char
    elif char in ignoreChars:
      pass
    elif not separated:
      hyperclean += ' '

  return re.sub(spaceSaver, ' ', hyperclean.strip().lower())


for line in args.infile:
  tweet = json.loads(line)
  args.outfile.write(clean_tweet(tweet[u"text"]) + " ")
