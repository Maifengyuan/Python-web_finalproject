import requests
import json
import pandas as pd
Mai_key = "217fc9b3f26daa32adb8c391fe0a372f"

# 天气查询
def weatherInfo(key,city):
    url = "https://restapi.amap.com/v3/weather/weatherInfo?parameters"
    parameters = {
        "key":Mai_key,
        "city":city
    }
    r = requests.get(url,params=parameters)
    return r.json()

# 地理编码
def geocode(key,address,city=None,batch=None,sig=None,output=None,callback=None):
    geo_url = "https://restapi.amap.com/v3/geocode/geo?parameters"
    """构造字典，名为parameters"""
    parameters = {
        "key":key,
        "address":address,
        "city":city,
        "sig":sig,
        "output":output,
        "callback":callback
    }
    response = requests.get(url=geo_url,params=parameters)
    return response.json()

# 逆地理编码
def regeo(key,location,poitype=None,radius=None,extensions=None,batch=None,roadlevel=None):
    regeo_url = "https://restapi.amap.com/v3/geocode/regeo?parameters"
    parameters = {
        "key":key,
        "location":location,
    }
    response = requests.get(url=regeo_url,params=parameters)
    return response.json()

# 路径规划
## 步行路径规划
def walking(key,origin,destination):
    walking_url = "https://restapi.amap.com/v3/direction/walking?parameters"
    parameters = {
        "key":Mai_key,
        "origin":origin,
        "destination":destination
    }
    response = requests.get(url=walking_url,params=parameters)
    return response.json()

## 公交路径规划
def integrated(key,origin,destination,city,cityd,strategy=None,nightflag=None,date=None,time=None):
    integrated_url = "https://restapi.amap.com/v3/direction/transit/integrated?parameters"
    parameters= {
        "key":Mai_key,
        "origin":origin,
        "destination":destination,
        "city":city,
        "cityd":cityd
    }
    response = requests.get(url=integrated_url,params=parameters)
    return response.json()

## 驾车路径
def driving(key,origin,destination):
    drive_url = "https://restapi.amap.com/v3/direction/driving?parameter"
    parameters = {
        "key":Mai_key,
        "origin":origin,
        "destination":destination
    }
    response = requests.get(url=drive_url,params=parameters)
    return response.json()

## 骑行路径
def bicycling(key,origin,destination):
    bicycle_url = "https://restapi.amap.com/v4/direction/bicycling?parameters"
    parameters = {
        "key":key,
        "origin":origin,
        "destination":destination
    }
    response = requests.get(url=bicycle_url,params=parameters)
    return response.json()

# 行政区域查询
def district(key,keywords,subdistrict=None):
    areas_url = "https://restapi.amap.com/v3/config/district?parameters"
    parameters ={
        "key":key,
        "keywords":keywords,
        "subdistrict":"3",
    }
    r = requests.get(url=areas_url,params=parameters)
    return r.json()

# 搜索POI
## 关键字搜索
def text(key,keywords,types,city):
    POI_url = "https://restapi.amap.com/v3/place/text?parameters"
    parameters = {
        "key":Mai_key,
        "keywords":keywords,
        "types":types,
        "city":city
    }
    r = requests.get(url=POI_url,params=parameters)
    return r.json()


## 周边搜索
def around(key,location):
    around_url = "https://restapi.amap.com/v3/place/around?parameters"
    params_around = {
        "key":key,
        "location":location
    }
    r = requests.get(url=around_url,params=params_around)
    return r.json()

## 多边形查询
def place(key,polygon):
    polygon_url = "https://restapi.amap.com/v3/place/polygon?parameters"
    parameters = {
        "key":Mai_key,
        "polygon":polygon
    }
    r = requests.get(url=polygon_url,params=parameters)
    return r.json()

## ID查询
def ID(key,id):
    id_url = "https://restapi.amap.com/v3/place/detail?parameters"
    parameters = {
        "key":key,
        "id":id
    }
    r = requests.get(url=id_url,params=parameters)
    return r.json()

# IP定位
def ip(ip):
    IP_url = "https://restapi.amap.com/v3/ip?parameters"  # api服务地址（请查看文档）
    parameters = {
        "key":Mai_key,
        "ip":ip
    }
    r = requests.get(url=IP_url,params=parameters)
    return r.json()

# 坐标转换
def convert(locations,coordsys=None):
    url = "https://restapi.amap.com/v3/assistant/coordinate/convert?parameters"
    parameters = {
        "key":Mai_key,
        "locations":locations,
        "coordsys":coordsys
    }
    r = requests.get(url,params=parameters)
    return r.json()

# 输入提示
def inputtips(keywords):
    url = "https://restapi.amap.com/v3/assistant/inputtips?parameters"
    parameters = {
        "key":Mai_key,
        "keywords":keywords
    }
    r = requests.get(url,parameters)
    return r.json()

### 交通态势权限不足

# 静态地图
# from PIL import Image
# from io import BytesIO
# import requests

def staticmap(location,zoom,size=None,scale=1,markers=None,labels=None,paths=None,traffic=0,page=None,sig=None):
    smap_url = "https://restapi.amap.com/v3/staticmap?parameters"
    params = {
    "key":Mai_key,
    "location":location,
    "zoom":zoom,
    "size":size,
    "markers":markers,
    'labels':labels,
    'paths':paths,
    'traffic':traffic,
    'sig':sig,
    'output':'json'
    }
    response = requests.get(smap_url,params=params)
    data = Image.open(BytesIO(response.content))
    return data

### 批量请求接口，地理围栏，轨迹纠偏省略


