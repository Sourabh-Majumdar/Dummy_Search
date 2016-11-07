# This program aims at counting the number of links in the final-List.txt
fhandle = open('final-List.txt')
i = 0
for line in fhandle :
    i = i + 1
print 'the number of lines are :',i
fhandle.close()
