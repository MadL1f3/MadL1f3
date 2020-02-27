import jsonpath
import requests
import json
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_python%E7%88%AC%E8%99%AB/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput='
}
data = {
    'first': 'true',
    'pn': 2,
    'kd': 'django开发'

}
session = requests.session()
session.get('https://www.lagou.com/jobs/list_python%E7%88%AC%E8%99%AB',headers=headers)
cookes = session.cookies
# print(cookes.get_dict())
req = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
res = requests.post(req,data=data,headers=headers,cookies=cookes).json()
# res = res.get("content")
a = res['content']['positionResult']['result']
for b in a:
    c = b
    print(b)
print(res)
# print(jsonpath.jsonpath(res,'$..companyLabelList'))