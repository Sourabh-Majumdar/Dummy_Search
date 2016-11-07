# This is the updated model for the Spider module which I constructed
# The advantage that it has over the previous module that it writes simultaneously
# While continuing to crawl the web
# This is the Crawler Module which has only one Job , i.e :
# Crawl the Web and find as many useful links as possible
import urllib
import time
from BeautifulSoup import *
final_list = list()
domain_list = [".com"]
special_list = ["news","india","latest"]
fhandle = open('final-List.txt','r+b')
for line in fhandle :
    links = line.split("\n")          
    final_list.append(links)            
def find_newlinks(all_links) :
    for link in all_links :
        string = link.get('href',None)
        if (string != None ) :
            if (analyse_string(string)) :
                if (final_list.count(string) == 0) :
                    final_list.append(string)
                    fhandle.write(string+"\n")
def analyse_string(string) :
    value = False
    if ("http" in string) :
        if ("://www" in string) :
            for domain in domain_list :
                if (domain in string) :
                    for special in special_list :
                        if (special in string ) :
                            value = True;
    return value
# -------------------------------------------------------------------------- // -----------------------------------------------------------------------------#
root = raw_input('Enter Site : ')
special_string = raw_input('If you want to keep this search very personal , provide the primary key , each followed by a comma ')
special_strings = special_string.split(",")
for key in special_strings :
    special_list.append(key)
htm = urllib.urlopen(root)
refined = BeautifulSoup(htm)
tags = refined('a')
find_newlinks(tags)
tags = refined('link')
find_newlinks(tags)
limit = int(raw_input('Enter a limiting value'))
n = 0
while n < limit and n < len(final_list) :
    try :
        new_source = final_list[n]
        html = urllib.urlopen(new_source)
        page = BeautifulSoup(html)
        all_links = page('a')
        find_newlinks(all_links)
        all_links = page('link')
        find_newlinks(all_links)
        n = n + 1
    except :
        n = n + 1
# -------------------------------------------------------------------------- // -----------------------------------------------------------------------------#
fhandle.close()
time.sleep(100)   
