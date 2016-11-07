# This program creates the number of outlinks for all the links in the final-List.txt
# So that using this I can upload this program on matlab and the computation becomes entirely mathematical
import urllib
from BeautifulSoup import *
file_handle = open('final-List.txt')
write_handle = open('link-outlink.txt','a')
matrix_handle = open('dataset.txt','a')
final_list = list()
for line in file_handle :                    # Here we load the previous list of links and append it to a temporary list
    links = line.split("\n")             # because for the first iteration we want to check if the spider returns any previously existing link in the existing
    final_list.append(links[0])             # database
def generate_list(size) :
    new_list = list()
    for i in range(0,size) :              # This function genrates a list of FINITE elements , (mostly the length of the final list)
        new_list.append(0)
    return new_list
def set_links(links,val) :
    data = generate_list(len(final_list))
    for link in links :
        try :
            index = final_list.index(link)   # This function sets the given vslue at the specific index
            data[index] = val
        except :
            continue
    return data
def find_all_links(page) :
    all_links = list()
    tags = page('a')
    for tag in tags :
        link = tag.get('href',None)
        if (link != None) :
            if (link.startswith('http')) :      # This function opens a page and finds all the links on that web page
                all_links.append(link)
    tags = page('link')
    for tag in tags :
        link = tag.get('href',None)
        if (link != None) :
            if (link.startswith('http')) :
                all_links.append(link)
    return all_links
#print final_list
matrix_list = list()
for index in range(0,len(final_list)) :
    all_links = list()
    try :
        source = final_list[index]
        html = urllib.urlopen(source)
        page = BeautifulSoup(html)
        all_links = find_all_links(page)
        outlink =  len(all_links)
        data = set_links(all_links,outlink)
        matrix_list.append(data)
        write_handle.write(str(index)+" "+str(outlink)+"\n")
        matrix_handle.write(str(index)+" ")
        for val in data :
            matrix_handle.write(str(val)+" ")
        matrix_handle.write("\n")
    except :
        data = generate_list(len(final_list))
        matrix_handle.write(str(index)+" ")
        for val in data :
            matrix_handle.write(str(val)+" ")
        matrix_handle.write("\n")        
print matrix_list
file_handle.close()
write_handle.close()
matrix_handle.close()
    
