import numpy as np
#from scipy.fftpack import dct
from PIL import Image
import os
path="1.jpg"
def dct(a):
    A=zeros((32,32))#生成0矩阵
#    a=[[100,100,100,100,100,100,100,100],[100,100,100,100,100,100,100,100],[100,100,100,100,100,100,100,100],[100,100,100,100,100,100,100,100],[100,100,100,100,100,100,100,100],[100,100,100,100,100,100,100,100],[100,100,100,100,100,100,100,100],[100,100,100,100,100,100,100,100]]
    A = asarray(A)
    shape=A.shape[1]#获取维数
    for i in range(32):
        for j in range(32):
            if(i == 0):
                x=sqrt(1/shape)
            else:
                x=sqrt(2/shape)
            A[i][j]=x*cos(pi*(j+0.5)*i/shape)#与维数相关

    A_T=A.transpose()#矩阵转置
    Y1=matmul(A,a)#矩阵叉乘
    Y=matmul(Y1,A_T)
#    print(Y)
    return Y
def ahash(path):
    img = Image.open(path)
    img = img.resize((8,8)).convert('L')
    img = np.asarray(img)
#    print(Image.fromarray(img).show())
    print(img.shape)
    mean=np.mean(img)
    print(mean)
    ahash=""
    for w_i in range(img.shape[0]):
        for h_i in range(img.shape[1]):
            if(img[w_i][h_i]<=mean):
                ahash=ahash+"0"
            else:
                ahash=ahash+"1"
    ahash=hex(int(ahash,2))
    print(ahash)
    return ahash
def phash(path):
    img = Image.open(path)
    img = img.resize((32,32)).convert('L')
    img = np.asarray(img)
#    print(Image.fromarray(img).show())
    dct_img=dct(img)
    img=[]
    for i in range(8):
        for j in range(8):
            img.append(dct_img[i][j])
    img=np.asarray(img)
    mean=np.mean(img)
    phash=""
    for w_i in range(len(img)):
        if(img[w_i]<=mean):
            phash=phash+"0"
        else:
            phash=phash+"1"
    phash=hex(int(phash,2))
    print(phash)
    return phash
def dhash(path):
    img = Image.open(path)
    img = img.resize((9,8)).convert('L')
    img = np.asarray(img)
    dhash=""
    for w_i in range(img.shape[0]):
        for h_i in range(img.shape[1]-1):
            if(img[w_i][h_i]<=img[w_i][h_i+1]):
                dhash=dhash+"0"
            else:
                dhash=dhash+"1"
    dhash=hex(int(dhash,2))
    print(dhash)
    return dhash
def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        print("children",child)
        with open("ahash.txt","a") as f:
            str_in=str(child).split("/")[-1]+" "+str(ahash(child)[2:])+"\n"
            f.write(str_in)
        with open("dhash.txt","a") as f:
            str_in=str(child).split("/")[-1]+" "+str(dhash(child)[2:])+"\n"
            f.write(str_in)
        with open("phash.txt","a") as f:
            str_in=str(child).split("/")[-1]+" "+str(phash(child)[2:])+"\n"
            f.write(str_in)
#        ahash(child)
#        phash(child)
#        dhash(child)
eachFile("D:/2020网课资料/WEB搜索技术/第二次作业/pic/")