import requests
from lxml import etree
import threading
from queue import Queue
import json
import time
import urllib.request


url_or = 'https://beijing.8684.cn/'
headers = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)'}
datas = []
times = 1
ct = 1

def creatqueue():
    page_queue = Queue()
    data_queue = Queue()
    return page_queue, data_queue

def first(url_or):
    r = requests.get(url=url_or,headers=headers)
    tree = etree.HTML(r.text)
    nums = tree.xpath('//div[@class="bus_layer_content"][3]/div[@class="bus_layer_r"]/a/@href')
    # alphas = tree.xpath('//div[@class="bus_kt_r2"]/a/@href')
    # all = nums + alphas
    return nums

def second(all, page_queue):
    for num in all:
        print("开始爬取%s开头的公交路线"%num)
        url_fd1 = url_or + num
        print(url_fd1)
        r = requests.get(url=url_fd1,headers=headers)
        tree = etree.HTML(r.text)
        bus_names = tree.xpath('//div[@class="stie_list"]/a/@href')
        for bus_name in bus_names:
            url_last = url_or + bus_name
        # yield bus_names
            print("结束爬取%s公交线路"%bus_name)
            page_queue.put(url_last)
        print('*' * 20)
    return page_queue


class CrawlThread(threading.Thread):
    """docstring for CrawlThread."""

    def __init__(self, name, page_queue, data_queue):
        super(CrawlThread, self).__init__()
        self.name = name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.headers = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)'}

    def run(self):
        print('!!!!!%s____线程启动!!!!!'%self.name)
        while 1:
            global ct
            if not self.page_queue.empty():
                print("---开始爬取第%s页---"%ct)
                url = self.page_queue.get()
                r = requests.get(url=url, headers=self.headers)
                self.data_queue.put(r.text)
                print("---结束爬取第%s页---"%ct)
                ct += 1
            else:
                break
        print('!!!!!%s____线程结束!!!!!'%self.name)

class ParserThread(threading.Thread):
    """docstring for ParserThread."""

    def __init__(self, name, page_queue, data_queue, fp, lock):
        super(ParserThread, self).__init__()
        self.name = name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.fp = fp
        self.lock = lock

    def run(self):
        print('!!!!!%s____线程启动!!!!!'%self.name)
        while 1:
            if not self.page_queue.empty():
                data = self.data_queue.get()
                print("***开始解析第%s条内容***"%times)
                self.parse_content(data)
            else:
                break
        print('!!!!!%s____线程结束!!!!!'%self.name)

    def parse_content(self, data):
        tree = etree.HTML(data)
        busname = tree.xpath('string(//div[@class="bus_i_t1"]/h1/text())').replace('&nbsp', ' ')
        runtime = tree.xpath('//div[@class="bus_i_content"]/p[1]/text()')[0]
        money = tree.xpath('//div[@class="bus_i_content"]/p[2]/text()')[0]
        lastupdate = tree.xpath('//div[@class="bus_i_content"]/p[4]/text()')[0]
        topline = tree.xpath('string(//div[@class="bus_line_top "][1]/div/strong/text())')
        downline = tree.xpath('string(//div[@class="bus_line_top "][2]/div/strong/text())')
        line = tree.xpath('string(//div[@class="bus_line_site "])')
        item = {
                '公车号' : busname,
                '运行时间' : runtime,
                '票价' : money,
                '最后更新时间' : lastupdate,
                '上行线' : topline,
                '下行线' : downline,
                '站牌号' :line,
        }
        global times
        times += 1
        self.lock.acquire()
        self.fp.write(json.dumps(item, ensure_ascii=False) + '\n')
        print("***结束解析第%s条内容***"%times)
        self.lock.release()

g_crawl_list = []
g_parse_list = []

def creat_crawl_thread(page_queue, data_queue):
    crawlname = ['采集线程一号', '采集线程二号', '采集线程三号','采集线程四号', '采集线程五号', '采集线程六号', '采集线程七号','采集线程八号', '采集线程九号', '采集线程十号',
    '采集线程十一号', '采集线程十二号','采集线程十三号', '采集线程十四号','采集线程十五号', '采集线程十六号', '采集线程十七号','采集线程十八号', '采集线程十九号','采集线程二十号',
    ]
    for name in crawlname:
        tcrawl = CrawlThread(name, page_queue, data_queue)
        g_crawl_list.append(tcrawl)

def creat_parse_thread(page_queue, data_queue, fp, lock):
    parsename = ['解析线程一号', '解析线程二号', '解析线程三号','解析线程四号', '解析线程五号', '解析线程六号','解析线程七号', '解析线程八号', '解析线程九号','解析线程十号',
    '解析线程十一号', '解析线程十二号','解析线程十三号', '解析线程十四号','解析线程十五号', '解析线程十六号', '解析线程十七号','解析线程十八号', '解析线程十九号','解析线程二十号',
    '解析线程二十一号', '解析线程二十二号','解析线程二十三号', '解析线程二十四号','解析线程二十五号', '解析线程二十六号', '解析线程二十七号','解析线程二十八号', '解析线程二十九号','解析线程三十号',
    '解析线程三十一号', '解析线程三十二号','解析线程三十三号', '解析线程三十四号','解析线程三十五号', '解析线程三十六号', '解析线程三十七号','解析线程三十八号', '解析线程三十九号','解析线程四十号'
    ]
    for name in parsename:
        tparse = ParserThread(name, page_queue, data_queue, fp, lock)
        g_parse_list.append(tparse)

def main():
    page_queue, data_queue = creatqueue()
    a = first(url_or)
    second(a, page_queue)
    fp = open('北京公交车.json', 'a', encoding="utf8")
    creat_crawl_thread(page_queue, data_queue)
    lock = threading.Lock()
    creat_parse_thread(page_queue, data_queue, fp, lock)
    for crawl in g_crawl_list:
        crawl.start()
    for parse in g_parse_list:
        parse.start()

    for crawl in g_crawl_list:
        crawl.join()
    for parse in g_parse_list:
        parse.join()

    fp.close()
    print('主线程执行完毕~~~~~')

if __name__ == "__main__":
    main()
