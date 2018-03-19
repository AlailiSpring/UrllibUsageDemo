import urllib.request

# userAgentInfo设置了默认值，后续调用的时候如果不需要可以不写这个参数；
# 但是如果没有默认值，那么调用时，必须给个值带过来
def openAndSaveUrlInfo(url,filePath,userAgentInfo=""):
    '''网页可以直接爬取直接读信息，否则模拟为浏览器进行爬取'''
    file = urllib.request.urlopen(url)
    data="";
    state=file.getcode()
    if(state==200):
        # 网页可以直接爬取
        data = file.read();
    else:
        # 网页不可以直接爬取，模拟浏览器访问对应的网页
        headers=("User-Agent",userAgentInfo)
        opener=urllib.request.build_opener()
        opener.addheaders=[headers]
        data=opener.open(url).read();
        # 另外一种模拟读取的方式
        # req=urllib.request.Request(url)
        # req.add_header("User-Agent",userAgentInfo)
        # data=urllib.request.urlopen(req).read()
    fhandle = open(filePath, "wb")
    fhandle.write(data)
    fhandle.close();

