import nltk
import re
import sys

def str2pat(s_pattern):
	pattern = re.split('[ |\n]+', s_pattern)
	if not pattern[-1]: pattern.remove('')
	return pattern

def str2pw(s_pw):
	pw = []
	pw.append(int(s_pw[0]))
	pw.append(s_pw[1])
	pw.append([nltk.tag.str2tuple(t) for t in s_pw[2].split()])
	pw.append(int(s_pw[-1]))
	return pw

def isPossible(pattern, pw):
	tagged = pw[2]
	if len(pattern) != len(tagged): return False
	for i in range(len(pattern)):
		if pattern[i] != '$':
			if pattern[i][0] == '<' and pattern[i][-1] == '>':
				tag = pattern[i][1:-1]
				if tag != tagged[i][1]: return False
			else:
				word = pattern[i]
				if word != tagged[i][0]: return False
	return True

def query(pats, fn):
	pws = []
	f = open(fn, 'r')
	while True:
		l = f.readline()
		if not l: break
		s_pw = re.split('[,|\n]+', l)
		if not s_pw[-1]: s_pw.remove('')
		pw = str2pw(s_pw)
		for pat in pats:
			if isPossible(pat, pw):
				pws.append(pw)
				break
	f.close()
	return pws

def pws2prs(pws):
	prs = []
	for pw in pws:
		pr = []
		pr.append(pw[-1])
		pr.append(pw[-2])
		prs.append(pr)
	return prs

def rmvDup(prs):
	n_prs = []
	for pr in prs:
		if not pr in n_prs:
			n_prs.append(pr)
	return n_prs

def createCands(pos, tmp, cands, qrypat):
	if pos == len(qrypat): 
		if len(tmp) > 0: cands.append(tmp)
		return
	if qrypat[pos][0] == '{' and qrypat[pos][-1] == '}':
		s = int(qrypat[pos][1])
		e = int(qrypat[pos][-2])
		for i in range(s, e + 1):
			nextTmp = []
			for e in tmp: nextTmp.append(e)
			nextTmp.append(i)
			createCands(pos + 1, nextTmp, cands, qrypat)
	else:
		createCands(pos + 1, tmp, cands, qrypat)	

def qrypat2pats(qrypat):
	tmp = []
	cands = []
	createCands(0, tmp, cands, qrypat)
	pats = []
	if len(cands) == 0:
		pat = []
		for i in range(len(qrypat)):
			pat.append(qrypat[i])
		pats.append(pat)
	else:
		for cand in cands:
			i = 0
			pat = []
			for j in range(len(qrypat)):
				if qrypat[j][0] == '{' and qrypat[j][-1] == '}':
					for k in range(cand[i]):
						pat.append('$')
					i += 1
				else:
					pat.append(qrypat[j])
			pats.append(pat)
	return pats

def recommend(k, prs):
	topk = []
	prs.sort()
	n = len(prs) if len(prs) <= k else k
	while len(topk) < n:
		topk.append(prs.pop())
	return topk

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print ('usage: finder.py <query pattern>')
		sys.exit()
	qrypat = sys.argv[1]
	qrypat = qrypat.split()
	pats = qrypat2pats(qrypat)
	pws = query(pats, 'patdb')
	prs = pws2prs(pws)
	prs = rmvDup(prs)
	topk = recommend(5, prs)
	for e in topk: print (e)
	print ('finish...')
