import re
from nltk.corpus import brown

def brown2sents(fn):
	fw = open(fn, 'w')
	for sent in brown.sents():
		data = ''
		for i in range(len(sent)):
			data += sent[i]
			if i < len(sent) - 1: data += ' '
		data += '\n'
		fw.write(data)
	fw.close()

def clean(frn, fwn):
	fr = open(frn, 'r')
	fw = open(fwn, 'w')
	p = re.compile('[a-zA-Z]+[-a-zA-Z]*[\'a-zA-Z]*')
	while True:
		line = fr.readline()
		if not line: break
		tokens = p.findall(line)
		data = ''
		for i in range(len(tokens)):
			data += tokens[i]
			if i < len(tokens) - 1: data += ' '
		data += '\n'
		fw.write(data)
	fr.close()
	fw.close()
	
