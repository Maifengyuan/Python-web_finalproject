import requests 
from random import random

# 土味情话
def duwei():
    tuwei=dict()
    for i in range(5):
        url = "https://v1.alapi.cn/api/qinghua"
        payload = "format=json"
        headers = {'Content-Type': "application/x-www-form-urlencoded",
                      "token":'fKpRQWPeUWz0dLntRyPx' # 网站ALAPI中有说明，要通过会员中心获取
                  }
        response = requests.request("POST", url, data=payload, headers=headers)
        res1 = response.json()["data"]["content"]
        tuwei[i]=res1
    return tuwei