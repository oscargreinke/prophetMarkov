import numpy


def make_pairs(corpus):
	for i in range(len(corpus)-1):
		yield(corpus[i], corpus[i+1])


bible = open('roughbible.txt', encoding='utf8').read()
corpus = bible.split()
pairs = make_pairs(corpus)

words = {}
for word1, word2 in pairs:
	if word1 in words.keys():
		words[word1].append(word2)
	else:
		words[word1] = [word2]

firstWord = numpy.random.choice(corpus)
chain = [firstWord]
numWords = 100
for i in range(numWords):
	chain.append(numpy.random.choice(words[chain[-1]]))
gospel = ' '.join(chain)

newGospel = open("newGospel.txt", 'w')
newGospel.write(gospel)
newGospel.close()
