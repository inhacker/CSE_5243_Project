import sgmllib

###############################################################################
# ReutersParser - an SGML parser
###############################################################################
class ReutersParser(sgmllib.SGMLParser):
    """A class to parse text from Reuters SGML files."""

    def parse(self, s):
        """Parse the given string 's', which is an SGML encoded file."""
        self.docs = []
        self.feed(s)
        self.close()

    def get_parsed_docs(self):
      return self.docs

    def __init__(self, verbose=0):
        """Initialize an object, passing 'verbose' to the superclass."""

        sgmllib.SGMLParser.__init__(self, verbose)
        self.in_title = 0
        """Flag indicating whether or not we're parsing the title."""

        self.in_dateline = 0
        """Flag indicating whether or not we're parsing the dateline"""

        self.in_body = 0
        """Flag indicating whether or not we're parsing the body"""

        self.title = ""
        """Title of the document"""

        self.doc_id = 0
        """Document ID"""

        self.dateline = ""
        """Date line for the document"""

        self.body = ""
        """Body of the document"""
        
        self.topics = []
        self.in_topic = 0
        self.docs = []

    def handle_data(self, data):
        """Print out data in TEXT portions of the document."""

        if self.in_body:
            self.body += data
        

    ####
    # Handle the Reuters tag
    ####
    def start_reuters(self, attributes):
        """Process Reuters tags, which bracket a document. Create a new
        file for each document encountered.
        """

        for name, value in attributes:
            if name == "newid":
                self.doc_id = int(value)

    def end_reuters(self):
        
        
        # lets cleanup the topics variable a bit by converting to a list
        self.docs.append({'doc_id' : self.doc_id, 'title' : self.title, 'dateline': self.dateline, 'body' : self.body, 'topics' : self.topics})
        
        
        self.body = ""
        

    
    ####
    # Handle BODY tags
    ####
    def start_body(self, attributes):
        """Indicate that the parser is in the body portion of the document.
        """

        self.in_body = 1

    def end_body(self):
       """Indicate that the parser is no longer in the body portion of the
       document.
       """

       self.in_body = 0
   

###############################################################################
# Main Program
###############################################################################
import sys
import os
import os.path

if __name__ == '__main__':
    # Get the filename as the first argument of the program,
    # open and read the file.
    filename = sys.argv[1]
    f = open(filename, "r")
    s = f.read()

    # Create a text directory if one does not exist
    #if not os.path.isdir("text"):
    #    os.mkdir("text")

    # Parse the file and output the results
    parser = ReutersParser()
    parser.parse(s)
    print parser.get_parsed_docs()[0]