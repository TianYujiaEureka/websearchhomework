

import os,traceback
from PIL import Image,ImageFont,ImageDraw
form="png"

def mark(path):
    im = Image.open(path).convert('RGBA')
#新建一个空白图片,尺寸与打开图片一样
    txt=Image.new('RGBA', im.size, (0,0,0,0))
#设置字体
    fnt=ImageFont.truetype("HYXiaoBoNuanSongW.ttf", int(txt.size[0]*0.1))
#操作新建的空白图片>>将新建的图片添入画板
    d=ImageDraw.Draw(txt)
#在新建的图片上添加字体
    d.text((int(txt.size[0]-txt.size[0]*0.5),int(txt.size[1]-txt.size[1]*0.7)), "bangqiaoyan",font=fnt, fill=(255,255,255,255))
#合并两个图片
    out=Image.alpha_composite(im, txt)
    
    out.convert("RGB").save("{}mark.jpg".format(i))

        
for i in range(1,14):
    path="{}mark.jpg".format(i,form)
#    mark(path)
    img = Image.open(path)   
    print( img.size)
    new_w,new_h=img.size[0]/4,img.size[1]/4
    print(new_w,new_h)
    out = img.resize((int(new_w),int(new_h)))
    out.save("{}matkresize.{}".format(i,form))
    #打开图片