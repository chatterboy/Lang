import nltk
import sys

def tagFrom(sentence):
	tokens = nltk.word_tokenize(sentence)
	return nltk.pos_tag(tokens)

def ngramsFrom(n, tagged):
	m = len(tagged)
	ngrams = []
	for i in range(n, m + 1):
		ngram = []
		for j in range(i - n, i):
			ngram.append(tagged[j])
		ngrams.append(ngram)
	return ngrams

def s_ngramsFrom(ngrams):
	s_ngrams = []
	for i in range(len(ngrams)):
		s_ngram = ''
		for j in range(len(ngrams[i])):
			s_ngram += ngrams[i][j][0] + '/' + ngrams[i][j][1]
			s_ngram += ' ' if j < len(ngrams[i]) - 1 else ''
		s_ngrams.append(s_ngram)
	return s_ngrams

def d_ngramsFrom(ngrams):
	s_ngrams = s_ngramsFrom(ngrams)
	d_ngrams = {}
	for i in range(len(s_ngrams)):
		if not s_ngrams[i] in d_ngrams:
			d_ngrams[s_ngrams[i]] = [1, ngrams[i]]
		else:
			d_ngrams[s_ngrams[i]][0] += 1
	return d_ngrams

def writeTo(fw, d_ngrams):
	for k, v in d_ngrams.items():
		tps = v[1]
		for i in range(len(tps)):
			data = ''
			data += str(i + 1)
			data += ','
			data += tps[i][0]
			data += ','
			data += k
			data += ','
			data += str(v[0])
			data += '\n'
			fw.write(data)

def createPatDB(frn, fwn):
	fr = open(frn, 'r')
	d_ngrams = {}
	while True:
		ngram = fr.readline()
		if not ngram: break
		ngram = ngram.replace('\n', '')
		t_ngram = [nltk.tag.str2tuple(t) for t in ngram.split()]
		if not ngram in d_ngrams:
			d_ngrams[ngram] = [1, t_ngram]
		else:
			d_ngrams[ngram][0] += 1
	fr.close()
	fw = open(fwn, 'a+')
	writeTo(fw, d_ngrams)
	fw.close()

def writeNgramsTo(n, frn, fwn):
	fr = open(frn, 'r')
	fw = open(fwn, 'w')
	while True:
		sent = fr.readline()
		if not sent: break
		tagged = tagFrom(sent)
		ngrams = ngramsFrom(n, tagged)
		s_ngrams = s_ngramsFrom(ngrams)
		for s_ngram in s_ngrams:
			data = s_ngram
			data += '\n'
			fw.write(data)
	fr.close()
	fw.close()

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print ('usage: analyzer.py <corpus name> <pattern db name>')
		sys.exit()
	frn = sys.argv[1]
	fwn = sys.argv[2]
	f = open(fwn, 'w+')
	f.close()
	for i in range(2, 5):
		writeNgramsTo(i, frn, 'ngramdb')
		createPatDB('ngramdb', fwn)
	print ('complete to create pattern database')
		
		






























	
