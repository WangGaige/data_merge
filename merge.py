# -*- coding: utf-8 -*-
import os 
import linecache  

root = 'D:\\CODE_LAB\\PY\\merge\\data' 
file_names = os.listdir(root)
file_ob_list = []  
for file_name in file_names: 
    fileob = root + '\\' + file_name  
    file_ob_list.append(fileob)  
    print(fileob)

print
file_ob_list 

ldata = []

data = []

for file_ob in file_ob_list:  
    total_line = len(open(file_ob).readlines())

    line_num = 1
    for i in range(total_line):
        line = linecache.getline(file_ob, i)
        if line.startswith(' '):
            line=file_ob.split('\\')[-1].split('.')[-2]+line
            ldata.append(line)
f = open("D:/data1.txt", "w+")  

for i,p in enumerate(ldata):   
    f.write(str(p))        


f.close()
