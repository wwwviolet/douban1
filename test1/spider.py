#-*- coding = utf-8 -*-
#@Time : 2021/6/5 21:07
#@Author : lqw
#@File : spider.py
#@software : PyCharm


from bs4 import BeautifulSoup     #网页解析，获取数据
import re       #正则表达式，进行文字匹配
import sys
import urllib.request,urllib.error  #指定url,获取网页数据
import xlwt     #进行excel操作
import sqlite3  #进行SQLlite操作



def main():
    baseurl = "https://movie.douban.com/top250?start="
    #1，爬取网页
    datalist = getDate(baseurl)
    #2，解析数据
    # savepath = "豆瓣电影top250.xls"
    dbpath = "movie.db"
    #3，保存数据
    # saveDate(datalist,savepath)
    # askURL("https://movie.douban.com/top250?start=")
    #4.db数据
    savaDate2DB(datalist,dbpath)

#影片详情的规则，r,忽视特殊符号
findLink = re.compile(r'<a href="(.*?)">')             #compie，生成正则表达式对象，表示规则（字符串的模式）
#影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)      #re.S,忽略换行符
#影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
#影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#找到评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)',re.S)

#爬取网页
def getDate(baseurl):
    datalist = []

    for i in range(0,10):       #调用获取页面信息的函数，10次
        url = baseurl + str(i*25)
        html = askURL(url)      #保存获取到的网页源码


        #2，逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):    #查找符合要求的字符串，形成列表
            #print(item)        #测试：查看电影item全部信息
            data = []           #保存一部电影的全部信息
            item = str(item)
            #获取影片详情的链接
            link = re.findall(findLink,item)[0] #re库通过正则表达式查找指定的字符串
            data.append(link)                       #添加链接
            imgSrc = re.findall(findImgSrc,item)[0]

            data.append(imgSrc)                     #添加图片
            titles = re.findall(findTitle,item)     #片名可能只有一个中文名，没有外文名
            if(len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)         #添加中文名
                otitle = titles[1].replace(" / ","")    #去掉无关的符号
                data.append(otitle)         #添加外文名
            else:
                data.append(titles[0])
                data.append(' ')            #外国名字留空

            rating = re.findall(findRating,item)[0]
            data.append(rating)             #添加评分

            judegNum = re.findall(findJudge,item)[0]
            data.append(judegNum)           #添加评价人数

            inq = re.findall(findInq,item)
            if (len(inq) != 0):
                inq = inq[0].replace("。","")    #去掉句号
                data.append(inq)                #添加概述
            else:
                data.append(" ")                #留空

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)     #去掉<br/>
            bd = re.sub('/',"",bd)                      #替换/
            bd = re.sub(' / '," ",bd)             #替换 / 
            data.append(bd.strip())                     #去掉前后空格

            datalist.append(data)                       #把处理好的一部电影的信息放入datalist

    return datalist


#得到指定一个URL的网页内容
def askURL(url):
        head = {    #模拟浏览器头部信息，向服务器发送消息
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41"
        }
                                                                                                    #用户代理，表示告诉服务器，我们是什么类型的机器，浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）
        request = urllib.request.Request(url=url,headers=head)
        html = ""
        try:
            response = urllib.request.urlopen(request)
            html = response.read().decode("utf-8")
            #print(html)
        except urllib.error.URLError as error:
            #hasattr()函数用于判断对象是否包含对应的属性。
            if hasattr(error,"code"):
                print(error,"code")
            if hasattr(error,"reason"):
                print(error.reason)

        return html

#保存数据
def saveDate(datalist,savepath):
                                          #压缩
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建workbook对象
                                          #覆盖之前的内容
    sheet = book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)  # 创建工作表
    col = ("电影详情链接","图片链接","中文名","外文名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])           #列名字
    for i in range(0,250):
        # print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])    #数据

    book.save(savepath)  # 保存数据库
    print("save.....")


def savaDate2DB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            data[index] = '"'+data[index]+'"'
            sql = '''insert into movie250(info_link,pic_link,cname,ename,score,rated,instrodction,info)values(%s)'''%",".join(data)
        print(sql)
            # cur.execute(sql)
            # conn.commit()

    cur.close()
    conn.close()


def init_db(dbpath):
    sql = '''
        create table movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar ,
        ename numeric ,
        instroduction tetx,
        info text
        )
    ''' #创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
