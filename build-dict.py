import sys
import collections
import argparse
import codecs

# Parse arguments
parser = argparse.ArgumentParser(description='Convert tweet JSON to a simple text file')
parser.add_argument('threshold', nargs='?', type=int, default=5, help='Minimum number of occurrences for a word to be included in the dictionary')
parser.add_argument('infile', nargs='?', type=lambda s: codecs.open(s, 'r', 'utf-8'), default=codecs.getreader('utf-8')(sys.stdin))
parser.add_argument('outfile', nargs='?', type=lambda s: codecs.open(s, 'w', 'utf-8'), default=codecs.getreader('utf-8')(sys.stdout))
args = parser.parse_args()

c = collections.Counter(args.infile.read().split())

for x in c.most_common():
	if x[1] < args.threshold:
		break
	# args.outfile.write(x[0] + "\n")
	args.outfile.write(x[0] + "\t" + str(x[1]) + "\n")
