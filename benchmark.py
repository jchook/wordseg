# pip install wordsegment
# 
from wordseg import segment as wordseg
from wordsegment import segment
import timeit

def test_wordseg():
	for hashtag in hdata:
		wordseg(hashtag)

def test_wordsegment():
	for hashtag in hdata:
		segment(hashtag)

hdata = open('hashtags.txt').read().split()

n = 100

print("==wordseg==\t\t==wordsegment==")

for hashtag in hdata:
	print("[" + " ".join(wordseg(hashtag)[0]) + "]\t\t[" + " ".join(segment(hashtag)) + "]")

print("==wordseg==\t\t==wordsegment==")

print(
	str(timeit.timeit("test_wordseg()", number=n, setup="from __main__ import test_wordseg")) + "\t\t" +
	str(timeit.timeit("test_wordsegment()", number=n, setup="from __main__ import test_wordsegment"))
)