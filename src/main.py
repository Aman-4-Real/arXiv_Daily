# -*- encoding: utf-8 -*-
'''
@Date     : 2021.11.19
@Author   : Aman
@Contact  : cq335955781@gmail.com
'''

import datetime
import json
import os

import uvicorn as u
from fastapi import FastAPI, Form
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from configs import keywords

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def read_data(rfile):
    with open(rfile, 'r') as f:
        data = json.load(f)
    return data


@app.get("/")
async def main(request: Request):
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(now_time + " _Request_")
    res = {}
    cnt = 0
    dedup = {}
    for _, dirs, files in os.walk("/home/caoqian/arxiv_daily/data/"):
        files = list(sorted(files))[::-1]
        for file in files:
            # print(file)
            date_name = file.split('.')[0]
            data = dict()
            data = dict(data, **read_data("/home/caoqian/arxiv_daily/data/" + file))
            for item in data:
                if data[item]['title'] not in dedup:
                    data[item]['title'] = data[item]['title'].replace('Title:', '')
                    data[item]['authors'] = data[item]['authors'].replace('Authors:', '')
                    data[item]['abstract'] = data[item]['abstract'].replace('Abstract: ', '').replace('\n', ' ')
                    dedup[data[item]['title']] = 1
                    cnt += 1
            res[date_name[:4] + '-' + date_name[4:6] + '-' + date_name[6:8]] = data
    res_idx = list(sorted(res.keys()))[::-1]
    # print(files, res_idx)
    return templates.TemplateResponse("arxiv_daily.html", {"request": request, "res": res, "res_idx": res_idx, "keywords": keywords, "cnt": cnt})


if __name__ == '__main__':
    u.run(app, host="0.0.0.0", port=9002)
