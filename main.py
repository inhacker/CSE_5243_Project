import sgmllib

#### start project

class ParserSgm(sgmllib.SGMLParser):
	def __init__(self, verbose=0):

		sgmllib.SGMLParser.__init__(self, verbose)

		self.doc = []
		self.doc_id = 0
		self.body_count = 0
		self.body = ""
		self.in_topic = 0
		self.topic = ""

	def get_docs(self):
		return self.doc

	def parse(self, s):
		self.feed(s)
		self.close()

	# def start_title(self, attributes):
	# 	self.title = 1
	# def end_title(self):
	# 	self.title = 0

	# def start_dateline(self, attributes):
	# 	self.dateline = 1
	# def end_dateline(self):
	# 	self.dateline = 0

	def start_topics(self, attributes):
		self.in_topic = 1
	def end_topics(self):
		self.in_topic = 0

	def start_body(self, attributes):
		self.body_count = 1
	def end_body(self):
		self.body_count = 0 

	def start_reuters(self, attributes):
		for name, value in attributes:
			if name == "newid":
				self.doc_id = int(value)

	def end_reuters(self):

		self.doc.append({'body': self.body, 'topic': self.topic, 'doc_id': self.doc_id})
		#print len(self.doc)
		# self.topics = 0
		# self.title = 0
		# self.dateline = 0
		self.body = ""
		self.body_count = 0

	def handle_data(self, data):
		if self.body_count == 1:
			self.body += data
		elif self.in_topic == 1:
			self.topic += data

############## Main Program ##################
import sys
import string
import operator

if __name__ == '__main__':
	total_parsed_article = []

	for x in ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]:
		file_name = "reut2-0" + x + ".sgm"
		
		f = open(file_name, "r")
		s = f.read()

		parser = ParserSgm();
		parser.parse(s)
		docs = parser.get_docs()
		for i in range(0, len(docs)):
			total_parsed_article.append(docs[i])
#print total_parsed_article[1]

stopwords = ['a', 'about', 'above', 'across', 'after', 'afterwards']
stopwords += ['again', 'against', 'all', 'almost', 'alone', 'along']
stopwords += ['already', 'also', 'although', 'always', 'am', 'among']
stopwords += ['amongst', 'amoungst', 'amount', 'an', 'and', 'another']
stopwords += ['any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere']
stopwords += ['are', 'around', 'as', 'at', 'back', 'be', 'became']
stopwords += ['because', 'become', 'becomes', 'becoming', 'been']
stopwords += ['before', 'beforehand', 'behind', 'being', 'below']
stopwords += ['beside', 'besides', 'between', 'beyond', 'bill', 'both']
stopwords += ['bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant']
stopwords += ['co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de']
stopwords += ['describe', 'detail', 'did', 'do', 'done', 'down', 'due']
stopwords += ['during', 'each', 'eg', 'eight', 'either', 'eleven', 'else']
stopwords += ['elsewhere', 'empty', 'enough', 'etc', 'even', 'ever']
stopwords += ['every', 'everyone', 'everything', 'everywhere', 'except']
stopwords += ['few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first']
stopwords += ['five', 'for', 'former', 'formerly', 'forty', 'found']
stopwords += ['four', 'from', 'front', 'full', 'further', 'get', 'give']
stopwords += ['go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her']
stopwords += ['here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers']
stopwords += ['herself', 'him', 'himself', 'his', 'how', 'however']
stopwords += ['hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed']
stopwords += ['interest', 'into', 'is', 'it', 'its', 'itself', 'keep']
stopwords += ['last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made']
stopwords += ['many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine']
stopwords += ['more', 'moreover', 'most', 'mostly', 'move', 'much']
stopwords += ['must', 'my', 'myself', 'name', 'namely', 'neither', 'never']
stopwords += ['nevertheless', 'next', 'nine', 'no', 'nobody', 'none']
stopwords += ['noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of']
stopwords += ['off', 'often', 'on','once', 'one', 'only', 'onto', 'or']
stopwords += ['other', 'others', 'otherwise', 'our', 'ours', 'ourselves']
stopwords += ['out', 'over', 'own', 'part', 'per', 'perhaps', 'please']
stopwords += ['put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed']
stopwords += ['seeming', 'seems', 'serious', 'several', 'she', 'should']
stopwords += ['show', 'side', 'since', 'sincere', 'six', 'sixty', 'so']
stopwords += ['some', 'somehow', 'someone', 'something', 'sometime']
stopwords += ['sometimes', 'somewhere', 'still', 'such', 'system', 'take']
stopwords += ['ten', 'than', 'that', 'the', 'their', 'them', 'themselves']
stopwords += ['then', 'thence', 'there', 'thereafter', 'thereby']
stopwords += ['therefore', 'therein', 'thereupon', 'these', 'they']
stopwords += ['thick', 'thin', 'third', 'this', 'those', 'though', 'three']
stopwords += ['three', 'through', 'throughout', 'thru', 'thus', 'to']
stopwords += ['together', 'too', 'top', 'toward', 'towards', 'twelve']
stopwords += ['twenty', 'two', 'un', 'under', 'until', 'up', 'upon']
stopwords += ['us', 'very', 'via', 'was', 'we', 'well', 'were', 'what']
stopwords += ['whatever', 'when', 'whence', 'whenever', 'where']
stopwords += ['whereafter', 'whereas', 'whereby', 'wherein', 'whereupon']
stopwords += ['wherever', 'whether', 'which', 'while', 'whither', 'who']
stopwords += ['whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with']
stopwords += ['within', 'without', 'would', 'yet', 'you', 'your']
stopwords += ['yours', 'yourself', 'yourselves']

def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]



body_example = total_parsed_article[1]["body"]

def removePunctuation(s):
  puncArray = list(string.punctuation)
  for punc in puncArray:
    s  = s.replace(punc, ' ')

  return s

body_example_str = removePunctuation(body_example)
body_list = body_example_str.split()
body_list_removed = removeStopwords(body_list, stopwords)


#print body_list_removed
body_freq = []

def makeDictionary():
	dictionary = dict()
	for w in body_list_removed:
		if w not in dictionary:
	   		dictionary[w] = 1
	   	else:
	   		dictionary[w] += 1
	return dictionary

#print dictionary
dictionary = makeDictionary()
sorted_dict = sorted(dictionary.items(), key = lambda k : k[1])

print sorted_dict


# def sortFreqDict(freqdict):
# 	aux = [(key, freqdict[key]) for key in freqdict]
# 	aux.sort()
# 	#aux.reverse()
# 	return aux

# sorted_dict = sortFreqDict(dictionary)
# print sorted_dict
#print ("pairs\n" + str(zip(body_list_removed, body_freq)))







