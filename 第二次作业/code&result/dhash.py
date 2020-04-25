# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 03:11:20 2020

@author: Eureka
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 00:34:13 2020

@author: Eureka
"""
def hammingDistance(x, y):
    """
        :type x: int
        :type y: int
        :rtype: int
    """
    count = 0
    while True:
        if (x == 0 and y == 0):
            break
        x, x_mod = divmod(x, 2)
        y, y_mod = divmod(y, 2)
        if x_mod != y_mod:
            count += 1
    return count
picname=[]
picdhash=[]

with open("dhash.txt",'r') as f:
    for lines in f:
        picname.append(lines.strip('\n').split(" ")[0])
        picdhash.append(lines.strip('\n').split(" ")[1])
print(picname," ",picdhash)
for i in range(1,14):
    dhash_goal=""
    pic="{}.jpg".format(i)
    for j in range(len(picname)):
        if(picname[j]==pic):
            print(j," is pic:",pic)
            dhash_goal=picdhash[j]
    print(dhash_goal)
    x=int(dhash_goal,16)
    dhash_dis=[]
    for j in range(len(picdhash)):
        y=int(picdhash[j],16)
        dhash_dis.append(hammingDistance(x,y))
    print(dhash_dis)
    result=sorted(range(len(dhash_dis)), key=lambda k: dhash_dis[k])
    str1=""
    with open("dhash_likemost.txt","a") as f:
        str1="和 "+picname[result[0]]+" 最像的 "
        f.write(str1)
        for j in range(1,11):
            f.write(str(j))
            f.write(": ")
            f.write(picname[result[j]])
            f.write("    ")
        f.write("\n")