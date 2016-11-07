# This is the updated model for the Spider module which I constructed
# The advantage that it has over the previous module that it writes simultaneously
# While continuing to crawl the web
# This is the Crawler Module which has only one Job , i.e :
# Crawl the Web and find as many useful links as possible
import urllib
import time
from BeautifulSoup import *
final_list = list()
domain_list = [".com",".org",".net",".co.in",".edu",".gov",".ac.in"]
special_list = ["news","india"]
fhandle = open('final-List.txt','r+b')
for line in fhandle :                    # Here we load the previous list of links and append it to a temporary list
    links = line.split("\n")             # because for the first iteration we want to check if the spider returns any previously existing link in the existing
    final_list.append(links)             # database
class Spider :
    def __init__(self,root,name,limit) :
        self.root = root
        self.name = name
        self.crawlinglinks = list()
        self.limit = limit
    def get_root(self) :
        return self.root
    def get_name(self) :
        return self.name
    def start_spidering(self) :
        htm = urllib.urlopen(self.root)
        refined = BeautifulSoup(htm)
        tags = refined('a')
        self.find_newlinks(tags)
        tags = refined('link')
        self.find_newlinks(tags)
        n = 0
        while n < self.limit and n < len(self.crawlinglinks) :
            try :
                new_source = self.crawlinglinks[n]
                html = urllib.urlopen(new_source)
                page = BeautifulSoup(html)
                all_links = page('a')
                self.find_newlinks(all_links)
                all_links = page('link')
                self.find_newlinks(all_links)
                n = n + 1
            except :
                n = n + 1
    def find_newlinks(self,all_links) :
        for link in all_links :
            string = link.get('href',None)             # This while loop has only one job , i.e to open all the links in the final list and add any new links it finds.
            if (self.analyse_string(string)) :           # The recent update is that it now directly adds a new link to the final-List.txt file and it searches only for a ".com" string
                if (final_list.count(string) == 0) and(self.crawlinglinks.count(string) == 0) :
                    final_list.append(string)
                    self.crawlinglinks.append(string)
                    fhandle.write(string+"\n")
    def analyse_string(self,string) :
        value = False
        if ("http" in string) :
            if ("://www" in string) :
                for domain in domain_list :
                    if (domain in string) :
                        for special in special_list :
                            if (special in string) :
                                value = True;
        return value
        
spiders = list()
number = int(raw_input('How many spiders are you keeping this time ?'))
for num in range(0,number) :
    name = raw_input('Name this spider :')
    root = raw_input('Give him his root url')
    limit = int(raw_input('Enter the limiting value :'))
    newSpider = Spider(root,name,limit)
    spiders.append(newSpider)
print 'Now lets make these guys start scrapping !!'
start_time = time.localtime(None)
for spider in spiders :
    spider.start_spidering()
fhandle.close()
end_time = time.localtime(None)
print start_time
print end_time
time.sleep(1200)   
