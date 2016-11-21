----SUBMISSION ITEMS AND OPERATING INSTRUCTIONS

1. code base in github

a. su - w205
b. git clone https://github.com/jenncasper/mids_w205_exercise2.git
c. run the four application deployment stages per the jenncasper_ex2_architecture.txt; make sure postgres server is running and crtl-c to quite each sparse command
   cd ./exercise2/EXTweetwordcount  
   sparse run --name tweetprint
   sparse run --name tweetparse
   sparse run --name tweetwordcount
   sparse run --name tweetwordcountdb

d. run the two serving scripts

   cd ../
   python finalresults.py hello
   python finalresults.py you
   python finalresults.py

   python histogram.py 3,8
   python histogram.py
   python histogram.py garbage,garbage

2. jenncasper_ex2_architecture.txt
3. directory called screenshots containing the screenshots referenced in this document
4. readme.txt 
5. plot.png
