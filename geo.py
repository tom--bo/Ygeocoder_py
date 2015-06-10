# http://qiita.com/Gen6/items/d63dc8f397f8cdc2dab7 写経からスタート
# -*- coding: utf-8 -*-
import requests
import json
import sys, codecs

def get_Coordinates(location_name):
    payload = {
        "appid": "YOUR ID", 
        "output":"json"
    }
    payload["query"] = location_name
    url = "http://geo.search.olp.yahooapis.jp/OpenLocalPlatform/V1/geoCoder"
    r = requests.get(url, params=payload)
    res = r.json()

    for i in res["Feature"]:
        print(i["Geometry"]["Coordinates"])

if __name__ == "__main__":
    get_Coordinates(u"東京都港区芝公園4‐2‐8")



