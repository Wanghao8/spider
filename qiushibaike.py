import urllib.request
import urllib.parse
import re
import os

url = "https://www.qiushibaike.com/imgrank/page/"

def main():

    start_page = int(input("请输入开始页数: "))
    end_page = int(input("请输入结束页数: "))
    list = range(start_page, end_page + 1)
    for page in list:
        url_page = url + str(page)
        headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'

        }
        handler = urllib.request.HTTPHandler()
        opener = urllib.request.build_opener(handler)
        request = urllib.request.Request(url=url_page, headers=headers)
        content = opener.open(request).read().decode('utf-8','ignore')
        # pattern = re.compile(r'<img src="(.*?)".*?>')
        pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)" .*?>', re.S)
        ret = pattern.findall(content)
        # print(ret)

        dirname = "糗图"
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        timeci = 1
        for image in ret:
            image = "http:" + image
            print("第%d张图开始下载。。。"%timeci)
            filename = image.split('/')[-1]
            filepath = dirname + '/' + filename
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(image, filepath)
            print("第%d张图停止下载。。。"%timeci)
            timeci += 1

if __name__ == '__main__':
    main()
