from com.python.selfDefinedFunc import openAndSaveUrlInfo

filePath="/Users/alailispring/PycharmProjects/crawlerFile/"

# -----------------------------------------------------------
# old ways of getting info from a website
# targetUrlAddr1="http://www.baidu.com"
# file=urllib.request.urlopen(targetUrlAddr1)
# data=file.read()
# dataLine=file.readline()
# print(dataLine)
# print(data)
# print(file.geturl())
# fhandle=open(filePath+"1.html","wb")
# fhandle.write(data)
# fhandle.close()
# -----------------------------------------------------------


# another way of writing info into a file with functions provided by urllib
# targetUrlAddr2="http://edu.51cto.com"
# newfile=urllib.request.urlretrieve(targetUrlAddr2,filePath+"2.html")


# -----------------------------------------------------------
url1="http://blog.csdn.net/a2Ni5KFDaIO1E6/article/details/78795609"

openAndSaveUrlInfo(url1,filePath+"4.html")
print(openAndSaveUrlInfo.__doc__)


