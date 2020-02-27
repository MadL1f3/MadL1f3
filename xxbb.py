from selenium import webdriver
import time
import requests


dirver = webdriver.Chrome()
dirver.get('https://yuba.douyu.com/p/877596621582313929')
sreach_windows = dirver.current_window_handle
dirver.maximize_window()

dirver.find_element_by_xpath('//*[@id="global_header_nav"]/div/div[2]/div[3]/a/span').click()
time.sleep(10)
dirver.refresh()
for x in range(1, 11, 2):
    time.sleep(0.5)
    j = x / 10
    js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f ' % j
    dirver.execute_script(js)
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'referer': 'https://yuba.douyu.com/p/877596621582313929',
}
while 1:
    re = 'https://yuba.douyu.com/wbapi/web/post/comments/877596621582313929?group_id=3270215&page=1&timestamp=0.6411702136681814'
    re = requests.get(re, headers=headers).json()
    a = re['comments_total']
    print(a)
    if a >199599:
        dirver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[3]').send_keys('给爸爸中')
        dirver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[3]/button').click()
    else:
        pass