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
picahash=[]

with open("ahash.txt",'r') as f:
    for lines in f:
        picname.append(lines.strip('\n').split(" ")[0])
        picahash.append(lines.strip('\n').split(" ")[1])
print(picname," ",picahash)
for i in range(1,14):
    ahash_goal=""
    pic="{}.jpg".format(i)
    for j in range(len(picname)):
        if(picname[j]==pic):
            print(j," is pic:",pic)
            ahash_goal=picahash[j]
    print(ahash_goal)
    x=int(ahash_goal,16)
    ahash_dis=[]
    for j in range(len(picahash)):
        y=int(picahash[j],16)
        ahash_dis.append(hammingDistance(x,y))
    print(ahash_dis)
    result=sorted(range(len(ahash_dis)), key=lambda k: ahash_dis[k])
    str1=""
    with open("ahash_likemost.txt","a") as f:
        str1="和 "+picname[result[0]]+" 最像的 "
        f.write(str1)
        for j in range(1,11):
            f.write(str(j))
            f.write(": ")
            f.write(picname[result[j]])
            f.write("    ")
        f.write("\n")