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
    if res.get("Feature"):
        for i in res["Feature"]:
            print(location_name + i["Geometry"]["Coordinates"])
    else:
        print(location_name + "null,null")

if __name__ == "__main__":
    args = sys.argv
    len = len(sys.argv)

    for i in range(1, len):
        dir = args[i]
        
        with open(dir, mode='r') as f:
            for line in f:
                line = line.replace('\n', ',')
                get_Coordinates(line)



