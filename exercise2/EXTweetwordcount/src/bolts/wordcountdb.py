from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2
import pprint

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
	
       	try:
            conn = psycopg2.connect(database="tcount", user="postgres", host="localhost", port="5432")
            self.log('effing bolt connected')
        except:
            #print "I am unable to connect to the database"
            self.log('effing bolt NOT connected')

        cur = conn.cursor()

        word = tup.values[0]

        # Write codes to increment the word count in Postgres
	cur.execute("SELECT count FROM Tweetwordcount WHERE word=%s", (word,))
	records = cur.fetchall()
	conn.commit()

	newVal = 0
	if records:
	    newVal = records[0][0]+1
	    self.log('there are records and newVal is %s' % newVal)
	    cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s", (newVal, word))
	    conn.commit()
	else:
	    newVal = 1
	    self.log('no effing records so newVal is %s' % newVal)
	    cur.execute("INSERT INTO Tweetwordcount (word, count) VALUES (%s, 1)", (word,))
	    conn.commit()

	# Use psycopg to interact with Postgres
        # Database name: Tcount 
        # Table name: Tweetwordcount 
        # you need to create both the database and the table in advance.

        # Increment the local count
	self.counts[word] == newVal
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
