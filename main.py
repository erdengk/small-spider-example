
import requests
import pymysql.cursors
import datetime

from bs4 import BeautifulSoup


# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='passwd',
    db='python',
    charset='utf8'
)
#数据条数
col=0

numOne=0
numOneFalse=0

numTwo=0
numTwoFalse=0

numThree=0
numThreeFalse=0
urlMap={'https://www.baidu.com/': '百度一下，你就知道'}
urlMapFalse={'https://www.baidu.com/': '百度一下，你就知道'}

# 获取游标
cursor = connect.cursor()
dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 根网站
url = 'https://www.baidu.com/'
strhtml = requests.get(url)
soup = BeautifulSoup(strhtml.text, 'html.parser')
dataOne = soup.select('a')


[s.extract() for s in soup("script")]
[s.extract() for s in soup("style")]

sIndex = soup.get_text().replace("'", "\\\'")

#爬取主页
try:
    sql = "INSERT into school(un_id,url,title,last_scan_time,parent_url,contents) values('%d','%s','%s',str_to_date(\'%s\','%%Y-%%m-%%d %%H:%%i:%%s'),'%s','%s')" \
          % \
          (0, "https://www.baidu.com/", soup.title.string, dt, url, sIndex)
    cursor.execute(sql)
    connect.commit()
    col = col + 1
except Exception as e:
    connect.rollback()  # 事务回滚
    print('网站首页处理失败', e)
    urlMapFalse[dataOne.get('href')] = dataOne.get_text()
    numOneFalse = numOneFalse + 1
else:
    connect.commit()  # 事务提交
    print('网站首页处理成功', cursor.rowcount)



#从主页开始遍历每一个url
for itemOne in dataOne:
    try:
        #以此判断当前链接是否已经爬取过、是否在失效url数组中、链接是否为空、链接是否有效，
        #当所有条件都通过时进行爬去
        if itemOne.get('href') not in urlMap:
            if itemOne.get('href') not in urlMapFalse:
                if itemOne.get_text() is not None:
                    if itemOne.get_text() is not "":
                        if itemOne.get('href') is not "":
                            if itemOne.get('href').startswith('http'):




                                urlTwo = itemOne.get('href')
                                strhtmlTwo = requests.get(urlTwo)
                                soupTwo = BeautifulSoup(strhtmlTwo.text, 'html.parser')
                                dataTwo = soupTwo.select('a')

                                #去除 代码字符，
                                [s.extract() for s in soupTwo("script")]
                                [s.extract() for s in soupTwo("style")]

                                #去除内容中的 '
                                sOne = soupTwo.get_text().replace("'", "\\\'")


                                sql = "INSERT into school(un_id,url,title,last_scan_time,parent_url,contents) values('%d','%s','%s',str_to_date(\'%s\','%%Y-%%m-%%d %%H:%%i:%%s'),'%s','%s')" \
                                      % \
                                      (1, itemOne.get('href'), itemOne.get_text(), dt, url,sOne)

                                cursor.execute(sql)
                                connect.commit()
                                col=col+1
                                #将新的url 放入去重
                                urlMap[itemOne.get('href')]=itemOne.get_text()
                                numOne=numOne+1

                                #开始爬取二级网站
                                try:
                                    for itemTwo in dataTwo:
                                        if itemTwo.get('href') not in urlMap:
                                            if itemTwo.get('href') not in urlMapFalse:
                                                if itemTwo.get_text() is not None:
                                                    if itemTwo.get_text() is not "":
                                                        if itemTwo.get('href') is not "":
                                                            if itemTwo.get('href').startswith('http'):


                                                                urlThree = itemTwo.get('href')
                                                                strhtmlThree = requests.get(urlThree)
                                                                soupThree = BeautifulSoup(strhtmlThree.text, 'html.parser')
                                                                dataThree = soupThree.select('a')


                                                                [s.extract() for s in soupThree("script")]
                                                                [s.extract() for s in soupThree("style")]
                                                                sTwo = soupThree.get_text().replace("'", "\\\'")

                                                                sql = "INSERT into school(un_id,url,title,last_scan_time,parent_url,contents) values('%d','%s','%s',str_to_date(\'%s\','%%Y-%%m-%%d %%H:%%i:%%s'),'%s','%s')" \
                                                                      % \
                                                                      (2, itemTwo.get('href'), itemTwo.get_text(), dt,urlTwo,sTwo)
                                                                cursor.execute(sql)
                                                                connect.commit()
                                                                col=col+1
                                                                urlMap[itemTwo.get('href')] = itemTwo.get_text()
                                                                numTwo = numTwo + 1

                                                                #开始爬取三级网站
                                                                try:
                                                                    for itemThree in dataThree:
                                                                        if itemThree.get('href') not in urlMap:
                                                                            if itemThree.get('href') not in urlMapFalse:
                                                                                if itemThree.get_text() is not None:
                                                                                    if itemThree.get_text() is not "":
                                                                                        if itemThree.get('href').startswith('http'):


                                                                                            urlFour = itemThree.get('href')
                                                                                            strhtmlFour = requests.get(urlFour)
                                                                                            soupFour = BeautifulSoup(strhtmlFour.text,'html.parser')
                                                                                            dataFour = soupFour.select('a')


                                                                                            [s.extract() for s in soupFour("script")]
                                                                                            [s.extract() for s in soupFour("style")]



                                                                                            sThree = soupFour.get_text().replace("'", "\\\'")

                                                                                            sql = "INSERT into school(un_id,url,title,last_scan_time,parent_url,contents) values('%d','%s','%s',str_to_date(\'%s\','%%Y-%%m-%%d %%H:%%i:%%s'),'%s','%s')" \
                                                                                                  % \
                                                                                                  (3, itemThree.get('href'), itemThree.get_text(), dt, urlThree,sThree)
                                                                                            cursor.execute(sql)
                                                                                            connect.commit()
                                                                                            col=col+1
                                                                                            numThree+=1
                                                                except Exception as e:
                                                                    connect.rollback()  # 事务回滚
                                                                    print('网站第三层处理失败', e)
                                                                    numThreeFalse+=1
                                                                    urlMapFalse[itemThree.get('href')] = itemThree.get_text()

                                                                else:
                                                                    connect.commit()  # 事务提交
                                                                    print('网站第三层处理成功', cursor.rowcount)
                                except Exception as e:
                                    connect.rollback()  # 事务回滚
                                    print('网站第2层处理失败', e)
                                    urlMapFalse[itemTwo.get('href')] = itemTwo.get_text()
                                    numTwoFalse+=1
                                else:
                                    connect.commit()  # 事务提交
                                    print('网站第2层处理成功', cursor.rowcount)
    except Exception as e:
        connect.rollback()  # 事务回滚
        print('网站第一层处理失败', e)
        urlMapFalse[itemOne.get('href')] = itemOne.get_text()
        numOneFalse=numOneFalse+1

    else:
        connect.commit()  # 事务提交
        print('网站第一层处理成功', cursor.rowcount)

print("总计爬取：%d"%col)
print('\n')
print("其中成功爬取1级网站：%d个"%numOne)
print("其中爬取1级网站失败：%d个"%numOneFalse)
print('\n')
print("其中成功爬取2级网站：%d个"%numTwo)
print("其中爬取2级网站失败：%d个"%numTwoFalse)
print('\n')
print("其中成功爬取3级网站：%d个"%numThree)
print("其中爬取3级网站失败：%d个"%numThreeFalse)
print('\n')

#print(urlMapFalse)



