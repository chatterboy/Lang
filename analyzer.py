import nltk

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
	fw = open(fwn, 'w')
	while True:
		sent = fr.readline()
		if not sent: break
		tagged = tagFrom(sent)
		for i in range(2, 5):
			ngrams = ngramsFrom(i, tagged)
			d_ngrams = d_ngramsFrom(ngrams)
			writeTo(fw, d_ngrams) 
	fr.close()
	fw.close()
