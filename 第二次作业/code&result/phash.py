# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 03:13:13 2020

@author: Eureka
"""

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
picphash=[]

with open("phash.txt",'r') as f:
    for lines in f:
        picname.append(lines.strip('\n').split(" ")[0])
        picphash.append(lines.strip('\n').split(" ")[1])
print(picname," ",picphash)
for i in range(1,14):
    phash_goal=""
    pic="{}.jpg".format(i)
    for j in range(len(picname)):
        if(picname[j]==pic):
            print(j," is pic:",pic)
            phash_goal=picphash[j]
    print(phash_goal)
    x=int(phash_goal,16)
    phash_dis=[]
    for j in range(len(picphash)):
        y=int(picphash[j],16)
        phash_dis.append(hammingDistance(x,y))
    print(phash_dis)
    result=sorted(range(len(phash_dis)), key=lambda k: phash_dis[k])
    str1=""
    with open("phash_likemost.txt","a") as f:
        str1="和 "+pic+" 最像的 "
        f.write(str1)
        for j in range(1,11):
            f.write(str(j))
            f.write(": ")
            f.write(picname[result[j]])
            f.write("    ")
        f.write("\n")