import requests
import json
from lxml import etree
from selenium import webdriver
import time


headers = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)'}
path = 'C:/users/14154/chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
brower = webdriver.Chrome(executable_path=path, chrome_options=options)

def parse(links):
    for link in links:
        link = link.get_attribute("href")
        response = requests.get(url=link, headers=headers)
        tree = etree.HTML(response.text)
        title = tree.xpath('//div[@class="summary-plane__content"]/h3/text()')
        money = tree.xpath('//div[@class="summary-plane__content"]/div/div/span/text()')
        city = tree.xpath('//div[@class="summary-plane__content"]//li/a/text()')
        experience = tree.xpath('//div[@class="summary-plane__content"]//li[2]/text()')
        education = tree.xpath('//div[@class="summary-plane__content"]//li[3]/text()')
        peoplenum = tree.xpath('//div[@class="summary-plane__content"]//li[4]/text()')
        welfare = tree.xpath('//div[@class="a-center-layout__content"]//div[@class="highlights__content"]/span/text()')
        describtion = tree.xpath('//div[@class="a-center-layout__content"]//div[@class="describtion__detail-content"]//text()')
        location = tree.xpath('//div[@class="a-center-layout__content"]//div[@class="job-address__content"]/span/text()')
        item = {
        '标题' : title,
        '薪水' : money,
        '工作城市' : city,
        '工作经验' : experience,
        '学历' : education,
        '招聘人数' : peoplenum,
        '福利' : welfare,
        '职位描述' : describtion,
        '工作地点' : location,
        }
        time.sleep(1)
        with open('zhilian.json', 'a', encoding='utf8') as fp:
            fp.write(json.dumps(item, ensure_ascii=False) + '\n')

def get_url(url):
    brower.get(url)
    time.sleep(3)
    links = brower.find_elements_by_xpath('//div[@class="contentpile"]/div/div/div/a')
    parse(links)

def main():
    page = 1
    url = 'https://sou.zhaopin.com/?p=%s&jl=719&sf=0&st=0&kw=python&kt=3'%page
    get_url(url)
    try :
        while brower.find_element_by_xpath('//button[@class="btn soupager__btn"]'):
            page += 1
            url = 'https://sou.zhaopin.com/?p=%s&jl=719&sf=0&st=0&kw=python&kt=3'%page
            get_url(url)
    except Exception:
        brower.quit()
    # fp.close()

if __name__ == '__main__':
    main()
