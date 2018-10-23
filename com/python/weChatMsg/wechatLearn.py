from wxpy import *
import requests

def get_news():

    """获取金山词霸每日一句，英文和翻译"""

    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note

bot=Bot()
# 给机器人自己发送消息
#bot.self.send('Hello World!')
# 给文件传输助手发送消息
#bot.file_helper.send('Hello World!')
#friends=bot.friends(update=False)
#for f in friends:
#    print(f)
contents=get_news()
print(contents[1])
friend=bot.friends().search(u'老婆')[0]
friend.send(contents[1]);
