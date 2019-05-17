import requests
from wxpy import *
from threading import Timer


bot = Bot(console_qr=2, cache_path="botoo.pkl")

def get_news1():
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    contents = r.json()['content']
    translation = r.json()['translation']
    return contents, translation

def send_news():
    try:
        my_friend = bot.friends().search(u'Hamdi')[0]
        my_friend.send(get_news1()[0])
        my_friend.send(get_news1()[1][5:])
        my_friend.send(u'来自Hamdi6919的心灵鸡汤！')
        t = Timer(60, send_news)
        t.start()
    except:
        my_friend = bot.friends().search('Hamdi')[0]
        my_friend.send(u'今天消息发送失败了')

if __name__ == '__main__':
    send_news()