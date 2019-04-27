from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import  pymysql
import hashlib
import datetime
#今日头条热点标题采集



driver = webdriver.Chrome() #加载浏览器控件
# driver.maximize_window()  #窗口最大化
# driver.minimize_window()  #窗口最小化
# time.sleep(1)
driver.set_window_size(850,1300)#窗口大小变化
driver.get('https://www.toutiao.com')  #打开头条

driver.find_element_by_class_name('login-button').click()
driver.implicitly_wait(10)
driver.find_element_by_class_name('login-type-icon').click()
driver.implicitly_wait(10)
driver.find_element_by_id('user-name').send_keys("2466980541@qq.com")
driver.implicitly_wait(10)
driver.find_element_by_id('password').send_keys("Jrtt@1234")
driver.implicitly_wait(10)
driver.find_element_by_id('bytedance-login-submit').click()
driver.implicitly_wait(10)
time.sleep(5)
driver.get('https://www.wukong.com/')  #打开头条
driver.find_element_by_link_text('热门').click()  #点击热点按钮
driver.implicitly_wait(10)

titles_list,comments_list,sources_list,times_list,hrefs_list=[],[],[],[],[]
def get_info():
        #获取标题
        titles=driver.find_elements_by_xpath('//div[@class="question-title"]/h2')
        for title  in   titles:
            titles_list.append(title.text)
            print(title.text)
        #获取来源
        sources = driver.find_elements_by_xpath('//span[@class="answer-info-user-name"]')
        for  source in sources:
            sources_list.append(source.text)
            print(source.text)
        #获取评论数
        comments=driver.find_elements_by_xpath('//span[@class="question-answer-num"]')
        for comment in comments:
            comments_list.append(comment.text)
            print(comment.text)
        #获取观看时间
        times=driver.find_elements_by_xpath('//span[@class="question-follow-num"]')
        for time in times:
            times_list.append(time.text)
            print(time.text)
        #获取该标题的链接
        urls=driver.find_elements_by_xpath('//div[@class="question-title"]/h2/a')
        for url in urls:
            url = url.get_attribute('href')
            hrefs_list.append(url)
            print(url)
#通过js加载更多的信息
def get_manyinfo():
    driver.execute_script("window.scrollTo(0,1000);")
    time.sleep(1)
    #爬取的数量控制
    while len(titles_list) < 500:
        for i in range(9):
            # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #js翻页方式
            driver.find_element_by_link_text('热门').send_keys(Keys.END)
            time.sleep(3)
        get_info()
        # save_info()
        driver.refresh()

    else:
        driver.quit()


def md5(str):
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    # print(m.hexdigest())
    return m.hexdigest()

def lanmu():
    lanmus = ['热点', '科技', '娱乐', '游戏', '体育', '汽车', '财经', '搞笑']
    # for i in range(len(a)):
    #     print(a[i])
    lanmu = random.choice(lanmus)
    print(lanmu)

#数据的保存
def  save_info():
    infos=zip(titles_list,hrefs_list,sources_list,comments_list,times_list)
    for info in infos:
        data={
            '标题':info[0],
            '链接':info[1],
            '来源':info[2],
            '评论':info[3],
            'time':info[4]
        }
        print(data)
        conn = pymysql.connect(host='localhost', user='root',passwd='aaa123321', port=3306, db='wukong')
        cur=conn.cursor()
        sql='replace into titles(title,href,source,comment,time_view,time_caiji,URL_UNIQUE) values (%s,%s,%s,%s,%s,%s,%s)'
        cur.execute(sql,(info[0],info[1],info[2],info[3],info[4],datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),md5(info[0])))
        conn.commit()
        conn.close()
if __name__ == '__main__':
    get_info()
    get_manyinfo()
    save_info()

#
# # 数据库
# -- phpMyAdmin SQL Dump
# -- version 4.0.10.19
# -- https://www.phpmyadmin.net
# --
# -- 主机: localhost
# -- 生成日期: 2019-04-26 07:34:30
# -- 服务器版本: 5.5.54
# -- PHP 版本: 5.4.45
#
# SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
# SET time_zone = "+00:00";
#
# --
# -- 数据库: `wukong`
# --
#
# -- --------------------------------------------------------
#
# --
# -- 表的结构 `titles`
# --
#
# CREATE TABLE IF NOT EXISTS `titles` (
#   `Id` int(10) NOT NULL AUTO_INCREMENT,
#   `title` mediumtext NOT NULL,
#   `href` varchar(1000) NOT NULL,
#   `source` text NOT NULL,
#   `comment` text NOT NULL,
#   `time_view` text NOT NULL,
#   `time_caiji` text NOT NULL,
#   `URL_UNIQUE` varchar(32) DEFAULT NULL,
#   PRIMARY KEY (`Id`),
#   UNIQUE KEY `URL_UNIQUE` (`URL_UNIQUE`),
#   KEY `href` (`href`(333))
# ) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;
