# This module is intended to show all the links
# Not only this but it also tries to maintain a register of all the words
import sqlite3
from BeautifulSoup import *
import urllib
file_handle = open("final-List.txt")
words = dict()
index = 0
conn = sqlite3.connect('linkTable.sqlite')
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS LINKS''')
cur.execute('''CREATE TABLE LINKS (link TEXT, link_number INTEGER)''')
def find_content(all_tags,attribute,index) :
        for iterator in all_tags :
            temp_content = iterator.get(attribute,None)
            if (temp_content != None) :
                content = temp_content.lower()
                value_list = words.get(content,None)          # We try to get/stirp the content from each meta tag and it compare it with the already existing
                if (value_list == None) :                     # list of words in our index and add it if it is new
                    value_list = list()
                    value_list.append(index)
                    words[content] = value_list
                else :
                    if (value_list.count(index) == 1) :
                        continue
                    else :
                        value_list.append(index)
                        words[content] = value_list
for line in file_handle :
    print line
    try :
        page = line.strip()
        display = urllib.urlopen(page)
        refined_display = BeautifulSoup(display)
        all_tags1 = refined_display('meta')
        all_tags2 = refined_display('h1')
        find_content(all_tags1,'content',index)
        find_content(all_tags2,'id',index)
        total_outlinks = find_outlinks(refined_display)
        cur.execute('''INSERT INTO LINKS (link,link_number) VALUES (?,?)''',(page,index))
        index = index + 1;
    except :
        continue
conn.commit()
file_handle.close()
file_handle = open('words-counter.txt','w')
for key in words :
    try :
        all_words = words.get(key)
        file_handle.write(key+" :-> ")
        for val in all_words :
            file_handle.write(str(val)+" ")
        file_handle.write("\n")
    except :
        continue
file_handle.close()

