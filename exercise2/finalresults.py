import sys
import psycopg2

def main(argv):

    try:
        conn = psycopg2.connect(database="tcount", user="postgres", host="localhost", port="5432")
    except:
        print "Unable to connect to the database"

    cur = conn.cursor()


    if len(argv) >= 2:
	word = argv[1]
        cur.execute("SELECT count FROM Tweetwordcount WHERE word=%s", (word,))
        records = cur.fetchall()
        conn.commit()

        if records:
            print("Total number of occurences of %s: %s" % (word, records[0][0]))
        else:
	    print("Total number of occurences of %s: not recorded in postgres" % word)
    else:
        cur.execute("SELECT * FROM Tweetwordcount ORDER BY word ASC")
	records2 = cur.fetchall()
	print (records2)

    conn.close()

if __name__ == "__main__":
    main(sys.argv)
