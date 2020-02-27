import re
import requests

session = requests.session()
def feach_url(url):
    print(session.get(url).content.decode('gb2312'))
    return session.get(url).content.decode('gb2312')

def id():
    
if __name__ == '__main__':
    url = 'https://wenku.baidu.com/view/7ff24ada91c69ec3d5bbfd0a79563c1ec4dad77e.html?from=search'
    feach_url(url)