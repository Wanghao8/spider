import urllib
import urllib.request
import urllib.parse
import os


url = "http://tieba.baidu.com/f?ie=utf-8&"
ba_name = input("请输入吧名：")
start_page = int(input("请输入开始页数: "))
end_page = int(input("请输入结束页数: "))
dirname = ba_name + "吧"
if not os.path.exists(dirname):
    os.mkdir(dirname)
for page in range(start_page, end_page+1):
    data = {
    'kw' : ba_name,
    'pn' : (page-1)*50
    }
    data = urllib.parse.urlencode(data)
    url_page = url + data

    headers = {"User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
    }
    request = urllib.request.Request(url=url_page, headers=headers)
    response = urllib.request.urlopen(request)
    print(url_page)
    print("第%s页开始下载。。。"%page)
    filename = ba_name + '_' + str(page) + ".html"
    filepath = dirname + '/' + filename
    with open(filepath, 'wb') as f:
        f.write(response.read())
    print("第%s页停止下载。。。"%page)
    f.close()
