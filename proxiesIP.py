import urllib
import urllib.request
import urllib.parse


url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=98050039_1_dg&wd=ip&rsv_pq=c37621980000d242&rsv_t=2e84wwaY%2B2LoLZQk7LQwlh3QKeNXBwljobU5uLV2kAzsgMm5VTfVA%2FTNgDYlqMENG7oMLA&rqlang=cn&rsv_enter=1&rsv_sug3=1"
handler = urllib.request.ProxyHandler({'https': '124.205.155.158:	9090'})
opener = urllib.request.build_opener(handler)
headers =  {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",}
request = urllib.request.Request(url = url, headers = headers)
response = opener.open(request)
with open('ip_address.html', 'wb') as pa:
    pa.write(response.read())
