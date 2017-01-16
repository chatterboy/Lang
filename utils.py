import re
from nltk.corpus import brown
from nltk.corpus import conll2000
from nltk.corpus import gutenberg

def gutenberg2Sents(fn):
	fw = open(fn, 'w')
	for sent in gutenberg.sents():
		data = ''
		for i in range(len(sent)):
			data += sent[i]
			if i < len(sent) - 1: data += ' '
		data += '\n'
		fw.write(data.lower())
	fw.close()

def conll2000ToSents(fn):
	fw = open(fn, 'w')
	for sent in conll2000.sents():
		data = ''
		for i in range(len(sent)):
			data += sent[i]
			if i < len(sent) - 1: data += ' '
		data += '\n'
		fw.write(data.lower())
	fw.close()

def brown2sents(fn):
	fw = open(fn, 'w')
	for sent in brown.sents():
		data = ''
		for i in range(len(sent)):
			data += sent[i]
			if i < len(sent) - 1: data += ' '
		data += '\n'
		fw.write(data.lower())
	fw.close()

def merge(fwn, fns):
	fw = open(fwn, 'a+')
	for fn in fns:
		fr = open(fn, 'r')
		while True:
			sent = fr.readline()
			if not sent: break
			fw.write(sent.lower())
		fr.close()
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
		fw.write(data.lower())
	fr.close()
	fw.close()
	
