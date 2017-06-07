import urllib
import urllib.request
import gzip
import http.cookiejar
from lxml import etree

url='https://www.douban.com/accounts/login'
##模拟浏览器访问
headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

##登录信息
p={
   'redir':'https://www.douban.com/',
    'form_email':'xxxxx',
    'form_password':'xxxxx',
   'login':u'登陆'
   }

##获取cookie
cookie=urllib.parse.urlencode(p).encode('utf-8')
cj=http.cookiejar.CookieJar()
op=urllib.request.HTTPCookieProcessor(cj)
opener=urllib.request.build_opener(op)

request=urllib.request.Request(url,cookie,headers)
data=opener.open(request)
#print(cookie)
##爬取每一页的科技话题数据，【标题】，【喜欢人数】以及【话题来源】
##查看数据为25页，循环25次
for i in range(25):
    get_url='https://www.douban.com/group/explore/tech?start='+str(30*i)
    request1=urllib.request.Request(get_url,headers=headers)
    req=opener.open(request1)
    text=req.read()
    data=gzip.decompress(text) ##解压文件

    html=etree.HTML(data)
    titles=html.xpath('//h3/a/text()')
    nums=html.xpath("//div[@class='likes']/text()[1]")
    authors=html.xpath("//span[@class='from']/a/text()")
    for j in range(len(titles)):
        print(titles[j]+' :  '+nums[j]+' '+'《'+authors[j]+'》')