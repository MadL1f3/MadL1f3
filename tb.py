import re
import time

from selenium import webdriver

def search_product():
    dirver.find_element_by_xpath('//*[@id="q"]').send_keys("python")
    dirver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
    time.sleep(10)
    token = dirver.find_element_by_xpath('//div[@class="total"]')
    token = str(token)
    token = int(re.compile('(\d+)').search(token).group(1))
    return token
def drop_down():
    for x in range(1,11,2):
        time.sleep(0.5)
        j = x/10
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f ' % j
        dirver.execute_script(js)

def get_prouct():
    divs = dirver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for div in divs:
        name = div.find_element_by_xpath('.//div[@class="row row-2 title"]/a').text
        all =div.find_element_by_xpath('.//div[@class="row row-1 g-clearfix"]').text

        print(name,all)

def next_page():
    token = search_product()
    drop_down()
    get_prouct()
    num = 1
    while num!= token:
        dirver.get('https://s.taobao.com/search?q=python&s={}'.format(44*num))
        dirver.implicitly_wait(10)#智能等待 最高为10s  超过 抛出异常
        num += 1
        drop_down()
        get_prouct()

if __name__ == '__main__':
    dirver = webdriver.Chrome()
    dirver.get('https://www.taobao.com/')
    next_page()