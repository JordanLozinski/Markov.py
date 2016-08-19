#markov

import re, random

chainlength = 2
stopword = "\x02"
maxwords = 30
markov = {}

def sanitize_message(message): #removes quotes from message and converts it all to lower case
    return re.sub('[\"\']', '', message.lower())

def parse_sentence(msg):
	msg = sanitize_message(msg)
	for w1, w2, w3 in split_message(msg):
		key = (w1, w2)
		if key in markov:
			markov[key].append(w3)
		else:
			markov[key] = [w3]

def split_message(msg):
	words = msg.split()

	if len(words) > chainlength:
		words.append(stopword)
		for i in range(len(words)-chainlength):
			yield words[i:i+chainlength+1]


def generate_message():
	key = random.choice(list(markov.keys()))
	seenwords = []
	for i in range(maxwords):
		seenwords.append(key[0])
		nextword = random.choice(markov[key])
		if nextword == stopword:
			break
		key = (key[1], nextword)
	return ' '.join(seenwords)