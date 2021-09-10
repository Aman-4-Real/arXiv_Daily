# -*- encoding: utf-8 -*-
'''
@Date     : 2021.09.10
@Author   : Aman
@Contact  : cq335955781@gmail.com
'''

import json
import time

import numpy as np
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from configs import keywords, urls

time_stamp = time.strftime("%Y%m%d",time.localtime())
print("Today is {}. Start crawling.".format(time_stamp))

abstract_urls = []
pdf_urls = []
print("Crawling urls...")
for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    websets = soup.find_all("span", class_="list-identifier")
    for webset in websets:
        links = webset.find_all("a")
        abstract_urls.append(links[0]["href"])
        pdf_urls.append(links[1]["href"])
    time.sleep(np.random.random() * 4 + 5)

store_data = {}
abstract_urls_failed = []
pdf_urls_failed = []
cnt = 0
print("Crawling item infos...")
for (abstract_url, pdf_url) in tqdm(zip(abstract_urls, pdf_urls)):
    abstract_url = "https://arxiv.org" + abstract_url
    pdf_url = "https://arxiv.org" + pdf_url
    try:
        r = requests.get(abstract_url)
    except:
        abstract_urls_failed.append(abstract_url)
        pdf_urls_failed.append(pdf_url)
        continue
    soup = BeautifulSoup(r.text, "html.parser")
    store = {}
    store["title"] = soup.find("h1", class_ = "title mathjax").text
    store["authors"] = soup.find("div", class_ = "authors").text
    store["submitted_date"] = soup.find("div", class_ = "dateline").text.strip()
    store["abstract"] = soup.find("blockquote", class_ = "abstract mathjax").text.strip()
    store["pdf_link"] = pdf_url
    flag = 0 # if kw in store
    for kw in keywords:
        if kw in store["title"].lower() or kw in store["abstract"].lower():
            flag = 1
    if flag:
        store_data[str(cnt)] = store
        cnt += 1
    time.sleep(np.random.random() * 4 + 5)
    

# store daily data
with open("../data/{}.json".format(time_stamp), "w") as f:
    store_data = json.dumps(store_data)
    f.write(store_data)
store_data = {}
print(f"Data saved to ../data/{time_stamp}.json.")
