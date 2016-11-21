from __future__ import absolute_import, print_function, unicode_literals

import re
from streamparse.bolt import Bolt

################################################################################
# Function to pass the original tweet string
################################################################################
class TweetPrint(Bolt):

    def process(self, tup):
        tweet = tup.values[0]  # extract the tweet

	# Emit the full tweet
	self.emit([tweet])

	# Log the tweet string to see the spout running
	self.log([tweet])

