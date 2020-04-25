"""
author:TianYujia
stuid 可以改为其他学生id
如果出现失败，可以通过更改starter从发生错误的位置上继续。
"""
import requests #导入requests模块
import time
import re
stuid=2017210421
b=stuid%19
print(b)
starter=(b-3)*150+1*150+63
ender=(b-3)*150+(b-2)*150+63
def spyder(i):
    url = 'http://win.bupt.edu.cn/program.do?id='+str(i)
    ###有些网站反爬虫，这里用headers把程序伪装成浏览器
    header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36' }
    ###登录需要提交的表单
    form_data = {'DDDDD':'2017210421', #填入学号
    'upass':'253323',  #填入校园网密码
    '0MKKey':''
    #'mode':'0',
    #'CookieDate':'0'
        }
    s = requests.session()
    response = s.post(url,data = form_data,headers = header)
    response =s.get(url,headers = header)
    response.encoding = 'utf-8'   
    a=response.text
    return a

def remy(str):
    title,info,entitle,college,source=-1,-1,-1,-1,-1
    str =str.replace('\n', '').replace('\r', '').replace("\xa0","")
#    print(str)
    matchObj_color = re.search( r'<h2>抱歉，没有该项目</h2>', str, re.M|re.I)
    
    if (matchObj_color!=None):
        return -1,-1,-1,-1,-1
    matchObj_title = re.search( r'<title>.*?</title>', str, re.M|re.I)
    if (matchObj_title!=None):
        title=matchObj_title.group().split("<")[-2].split(">")[-1]
        print(title)
    reInfo = re.compile(r'<br>\s*<div style="font-size:17px;line-height:25px;">\s*(.*?)(\s*</div>){7}', re.S)
    info=reInfo.search(str).group(1).replace("\r\n"," ").replace("\n"," ").replace("\r"," ")
    matchObj_entitle = re.search( r'<div style="margin-top:-7px;overflow: hidden;white-space: nowrap;text-overflow: ellipsis;">.*?</div>', str, re.M|re.I)
    if (matchObj_entitle!=None):
        entitle=matchObj_entitle.group().split("<")[-2].split(">")[-1]
        print(entitle)
    matchObj_college = re.search( r'<h3 style="display:inline;">&nbsp;.*?</h3>', str,re.M|re.I)
    if (matchObj_college!=None):
        college=matchObj_college.group().split("<")[-2].split("&nbsp;")[-1]
        
    matchObj_source = re.search( r'","name":".*?"}', str, re.M|re.I)
    if (matchObj_source!=None):
        source=matchObj_source.group().split("\"")[-2]
        print(source)
    return  title,info,entitle,college,source

def unicode2gbk(s):
    s=s.encode('utf-8').decode("unicode_escape")
    return s

for x in range(starter ,ender+1):
    a=str(spyder(x))
    a =a.replace('\n', '').replace('\r', '')
    title,info,entitle,college,source=remy(a)
    if(title==-1):
         continue
    filename = 'D:/webspyder/{}.txt'.format(x)
    with open(filename, 'w') as file_object:
        print(title)
        file_object.write("id:{0}\n".format(x))
        if(title!=-1):
            file_object.write("title:{}\n".format(title))
        if(entitle!=-1):
            file_object.write("en_title:{}\n".format(entitle).encode("gbk", 'ignore').decode("gbk", "ignore"))
        if(college!=-1):
            file_object.write("college:{}\n".format(college))
        if(info!=-1):
            file_object.write("info:{}\n".format(info).encode("gbk", 'ignore').decode("gbk", "ignore"))
        if(source!=-1):
            file_object.write("source:{}\n".format(unicode2gbk(source).split("评审")[0]))
#            print(a[0:100])
    time.sleep(1)
    print("sleep")
    time.sleep(1)
    print("sleep")
    time.sleep(1)
    print("sleep")
    