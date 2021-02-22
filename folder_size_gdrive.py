#First of all open a colab notebook and then mount your drive (/content/drive/Mydrive/)

#after mounting just run the following code/script in a cell

import re
all = open("all.txt", "w")
! du -h /content/drive/My\ Drive/* >> all.txt
all.close()
GB = open("GB.txt", "w")
for line in open("all.txt", "r"):
    if re.search("G\t", line):
        GB.write(line)
        print(line)
GB.close()
