import sgmllib

#### start project ########################
#class Parser to parse the article
class ParserSgm(sgmllib.SGMLParser):
	def __init__(self, verbose=0):

		sgmllib.SGMLParser.__init__(self, verbose)

		self.doc = []
		self.doc_id = 0
		self.body_count = 0
		self.body = ""
		self.in_topics = 0
		self.in_d=0
		self.topics = ""

	def get_docs(self):
		return self.doc

	def parse(self, s):
		self.feed(s)
		self.close()

	# def start_topics(self, attributes):
	# 	self.topics = 1
	# def end_topics(self):
	# 	self.topics = 0

	# def start_dateline(self, attributes):
	# 	self.dateline = 1
	# def end_dateline(self):
	# 	self.dateline = 0
	# start_ function can identify many tags like topics, body, reuters
	def start_d(self,attributes):
		if self.in_topics==1:
			self.in_d=1
	def end_d(self):
		self.in_d=0
		self.in_topics=0

	def start_topics(self, attributes):
		self.in_topics = 1
	def end_topics(self):
		self.in_topics = 0

	def start_body(self, attributes):
		self.body_count = 1
	def end_body(self):
		self.body_count = 0 

	def start_reuters(self, attributes):
		for name, value in attributes:
			if name == "newid":
				self.doc_id = int(value)

	def end_reuters(self):
		self.doc.append({'body': self.body, 'topics': self.topics, 'doc_id': self.doc_id})
		#print len(self.doc)
		
		self.topics = ""
		self.in_topics = 0
		# self.dateline = 0
		self.body = ""
		self.body_count = 0
	# deal with all the data between the tags
	def handle_data(self, data):
		if self.body_count == 1:
			self.body += data
		elif self.in_d == 1:
			self.topics+=data
##############################################

# collect all the words that is uncecessary in the article
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
stopwords += ['yours', 'yourself', 'yourselves','said','just']

def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]

def removePunctuation(s):
  puncArray = list(string.punctuation)
  for punc in puncArray:
    s  = s.replace(punc, ' ')

  return s

def removeDigitWords(s):
	new_s = ""
	wordlist = s.split()
	for word in wordlist:
		if not word.isdigit():
			new_s += word + " "
	return new_s

def makeDictionary(body_list,Fre):
	dictionary = dict()
	TF=dict()
	count=0
	for w in body_list:
		count+=1
		if w not in Fre:
			Fre[w]=0
		if w not in dictionary:
	   		dictionary[w] = 0
	   	Fre[w]+=1
	   	dictionary[w] += 1
	for i in dictionary:
		TF[i]=float(dictionary[i])/count

	return dictionary,TF
def removeTopic(body,topic):
	for i in range(0,len(body)):
		for y in body[i].keys():
			if y==topic[i]: 
				del body[i][y]

def chooseWord(body,n):
	wordlen=dict()
	pos=0
	for i in body:
		pos+=1
		print(pos)
		for j in i.keys():
			if j not in wordlen.keys():
				wordlen[j]=0
			wordlen[j]+=i[j]
	key,value=sorted(wordlen.items(),key=lambda k:k[1]).reverse()[0:n]
	return key


def tf_idf(TF,length,Fre,words):
	for i in TF:
		for j in i:
			i[j]*=log(length/1+Fre[j])
			if Fre[j]>110 and Fre[j]<5500:
				if j not in words:
					words[j]=0
				words[j]+=i[j]

def construct(source,words,topic,classes):
	result=[]
	dic=dict()
	classlen=dict()
	for n in classes:
		dic[n]=[0.1 for x in range(0,len(words))]
		classlen[n]=0.1

	for i in range(0,len(source)):
		tgt=[]
		filt=dic[topic[i]]
		classlen[topic[i]]+=1
		for j in range(0,len(words)):
			if words[j] in source[i]:
				tgt.append(source[i][words[j]])
				filt[j]+=1
			else:
				tgt.append(0)
		result.append(tgt)
	for n in dic:
		divid=classlen[n]
		for i in range(0,len(dic[n])):
			dic[n][i]/=divid
	length=len(source)
	for n in classlen:
		classlen[n]/=length
	return result,dic,classlen

def kNearestNeighbor(k,data,classes,test):
	result=array([0 for x in ])
	n=0
	for sample in test:
		candidate=set()
		arr=array([0 for x in range(0,len(data))])
		for i in range(0,len(data)):
			# print(data[i])
			# print(sample)
			arr.append([cosine(data[i],sample),classes[i]])
		temp=sorted(arr,key=lambda k:k[0])[0:k]
		result.append[vote(temp)]
	return result

# def cosine(vector1, vector2):  
#     dot_product = 0.0  
#     normA = 0.0  
#     normB = 0.0  
#     for a in vector1:
#     	for b in vector2:  
# 	        dot_product += a * b  
# 	        normA += a ** 2  
# 	        normB += b ** 2  
#     if normA == 0.0 or normB == 0.0:  
#         return None  
#     else:  
#         return dot_product / ((normA * normB) ** 0.5) 

def cosine(vector1,vector2):
	op7=np.dot(vector1,vector2)/(np.linalg.norm(vector1)*(np.linalg.norm(vector2)))  
	return op7  

def vote(temp):
	weight=dict()
	distance=dict()
	tgt=temp[0][1]
	for i in temp:
		if i[1] not in weight:
			weight[i[1]]=0
			distance[i[1]]=0
		weight[i[1]]+=1
		distance[i[1]]+=i[0]
		if i[1]!=tgt and weight[i[1]]>=weight[tgt]:
			if weight[i[1]]>weight[tgt] or distance[i[1]]<distance[tgt]:
				tgt=i[1]
	return tgt


#this is an one_vs_all classifier
def naiveBayes(dic,test,classlen):
	result=[]
	for sample in test:
			result.append(Result(dic,sample,classlen))
	return result

	# class_points=dict()
	# P=dict()
	# for i in range(0,len(labels)):
	# 	class_points[i]=[]
	# 	P[i]=[]
	# 	for i in range(0,len(data[0])):
	# 		gini=gini(data,classes,i,labels[i])
	# 		class_points[i].append(gini[0])
	# 		P[i].append([gini[1],gini[2]])
	
# def classes(topics,classes,data):
# 	n=dict()


# def possible(classes,data):
# 	dic=dict()
# 	count=dict()
# 	size=data!=0&&.size()
# 	for i in classes:
# 		if i not in count.keys():	
# 			count[i]=0
# 			dic[i]=[]
# 			for j in range(0,len(data[0])):
# 				dic[i].append(0.0)
# 		count[i]+=1
	
# 	for i in range(0,len(classes)):
# 		for j in range(0,len(i)):
# 			if i[j]!=0:
# 				dic[classes[i]][j]+=1
# 	for word in dic:
# 		C=count[word]
# 		for i in range(0,len(dic[word])):



def Result(P,sample,classlen):
	possible=dict()
	for i in P:
		possible[i]=1.0
	for i in range(0,len(sample)):
		if sample[i]!=0:
			for j in P:
				possible[j]*=P[j][i]
	for i in P:
		possible[i]*=pow(classlen[i],1)

	tgt=max(possible.values())
	pos=''
	for i in P:
		if possible[i]==tgt:
			pos=i
	return pos



############## Main Program ##################
import sys
import string
import operator
from numpy import *
from math import *

if __name__ == '__main__':

	outputfile = open("output.txt", "w")


	total_parsed_article = []
	# go through all the files we have and do preprocessing
	for x in ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]:
		file_name = "reut2-0" + x + ".sgm"
		
		f = open(file_name, "r")
		s = f.read()

		parser = ParserSgm();
		parser.parse(s)
		docs = parser.get_docs()
		for i in range(0, len(docs)):
			total_parsed_article.append(docs[i])
	#print total_parsed_article[0][]
	body=[]
	topic=[]
	TF_IDF=[]
	wordFre=dict()
	for i in range(0, len(total_parsed_article)):

		#print dictionary

		if total_parsed_article[i]["topics"]!="":
			body_example = total_parsed_article[i]["body"]
			body_example = removePunctuation(body_example)
			body_example = removeDigitWords(body_example)
			body_example = body_example.lower()
			body_list = body_example.split()
			body_list = removeStopwords(body_list, stopwords)
			dictionary,TFi = makeDictionary(body_list,wordFre)
			body.append(dictionary)
			TF_IDF.append(TFi)
			topic.append(total_parsed_article[i]["topics"])

		#print sorted_dict

	# 	outputfile.write(str(total_parsed_article[i]["doc_id"]))    
	# 	outputfile.write(" ")
	# 	outputfile.write(str(total_parsed_article[i]["topics"]))
	# 	outputfile.write(" ")
	# 	outputfile.write(str(sorted_dict))
	# 	outputfile.write("\n")
	# 	outputfile.write("\n")
	# outputfile.close()
	# removeTopic(body,TFi,topic)
	length=len(body)
	words=dict()
	tf_idf(TF_IDF,length,wordFre,words)
	# print(length)
	# print(len(wordFre))
	words=sorted(words.items(),key=lambda k:k[1])
	words.reverse()
	words=words[0:100]
	candidate=[]
	for i in words:
		candidate.append(i[0])
	# print(TF_IDF[0:10])
	KNNdata,dic,classlen=construct(body,candidate,topic,set(topic))

	print(classlen)
	pos=7*len(TF_IDF)/10
	# resultKNN=kNearestNeighbor(5,KNNdata[0:pos],topic[0:pos],KNNdata[pos:])
	resultNB=naiveBayes(dic,KNNdata[pos:],classlen)
	true=0
	false=0
	cmr=topic[pos:]
	for i in range(0,len(resultNB)):
		if resultNB[i]==cmr[i]:
			true+=1
		else:
			false+=1
	print(true)
	print(false)
	# words=set(wordFre.keys())-set(topic)
	# print(words)
	# tf,idf,tf_idf=TF_IDF(body)
	



# def cutsort(map,len):
# 	return_result=sorted(map.items(),key=lambda k:k[1]).reverse()[0:len]
# 	return return_result

	





# def gini(data,class,x,label)
# 	cal=[]
# 	m=0
# 	n=0
# 	for paper in data:
# 		if class[n++]==label:
# 			m+=1
# 			cal.append([paper[x],1])
# 		else:
# 			n+=1
# 			cal.append([paper[x],0])
					

# 	sorted_cal=sorted(cal,key=lambda x:x[0])
# 	gini=0.0
# 	pos=0
# 	for i in range(0,len(sorted_cal)):
# 		if sorted_cal[i][2]==1:
# 			class1+=1
# 		else:
# 			class0+=1
	
# 	return pos,class1>class0



