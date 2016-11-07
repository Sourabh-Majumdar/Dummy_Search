# This the Query module
# As soon as you type a query this searches a corresponding words in the already existing database
# If any link exists regarding the query then it will present it to you
import sqlite3
temp_query = raw_input('Enter Query :')
query_list = temp_query.lower().split()
file_handle = open('words-counter.txt')
conn = sqlite3.connect('linkTable.sqlite')
cur = conn.cursor()
for query in query_list :
    for line in file_handle :
        words = line.split(":->")
        key = words[0].strip()
        if (key == query) :
            all_links = words[1].split()
            for link in all_links :
                for row in cur.execute('''SELECT link FROM LINKS WHERE link_number = (?)''',(link,)) :
                    print str(row[0])

                        
