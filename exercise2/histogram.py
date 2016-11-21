import sys
import re
import psycopg2

pattern = re.compile("[0-9]+,[0-9]+")

def main(argv):

    if (len(argv) == 2) and (pattern.match(argv[1])):
	minInt = argv[1].split(',')[0]
	maxInt = argv[1].split(',')[1]
	print minInt, maxInt
    else:
	print "historgram.py MININT,MAXINT"
	return() 

    try:
        conn = psycopg2.connect(database="tcount", user="postgres", host="localhost", port="5432")
    except:
        print "Unable to connect to the database"

    cur = conn.cursor()

    cur.execute("SELECT word, count FROM Tweetwordcount WHERE count>=%s AND count <=%s ORDER BY count DESC", (minInt, maxInt))
    records = cur.fetchall()
    for rec in records:
	print rec[0], ": ", rec[1]

    conn.close()

if __name__ == "__main__":
    main(sys.argv)
