
import os
str=""
child=""
def eachFile(filepath):
    child=""
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        print("children",child)#文件夹中所有文件的文件名
        readFile(child)
def readFile(filename):
    str=""
    fopen = open(filename, 'r',encoding='gbk') # r 代表read#, encoding='UTF-8'
    try:
        str= fopen.read()
        file=r"D:/a2017210421/allin.txt"
        with open(file, 'a+') as f:
            f.write(str)
            f.close()
    finally:
        fopen.close()   
    return None

filepath="D:/a2017210421/a2017210421/"
eachFile(filepath)
    
    
