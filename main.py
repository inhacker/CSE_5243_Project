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
			total_parsed_article.append(parser.get_docs()[i])
#print total_parsed_article[1]

body_example = total_parsed_article[1]["body"]

print body_example
