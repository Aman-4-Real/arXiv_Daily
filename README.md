# arXiv_Daily
A toolkit for [arXiv](https://arxiv.org/) papers daily reading. The script will crawl arXiv papers in custom areas everyday and display key information.


## Structure
`data/`: Directory for crawled data. All data are named by datetime. The data format is like: 
```
"0": {
  "abstract": "",
  "authors": "",
  "pdf_link": "",
  "submitted_data": "",
  "title": ""
}
```

`src/`: Directory for codes and scripts. Containing:

- [`static/`](https://github.com/Aman-4-Real/arXiv_Daily/tree/main/src/static): Directory for static files. 
- [`templates/`](https://github.com/Aman-4-Real/arXiv_Daily/tree/main/src/templates): Directory for `.html` interface. 
- [`configs.py`](https://github.com/Aman-4-Real/arXiv_Daily/blob/main/src/configs.py): File of customized urls and keywords to be crawled. 
- [`daily_arxiv_spyder.py`](https://github.com/Aman-4-Real/arXiv_Daily/tree/main/src/daily_arxiv_spyder.py): Code for arXiv spiders. 
- [`keep_recent_data.py`](https://github.com/Aman-4-Real/arXiv_Daily/tree/main/src/keep_recent_data.py): Code for keeping the data of the last week only.
- [`log`](https://github.com/Aman-4-Real/arXiv_Daily/blob/main/src/log): Crontab log file.
- [`main.py`](https://github.com/Aman-4-Real/arXiv_Daily/tree/main/src/main.py): Code for fastapi interface.
- [`run.sh`](https://github.com/Aman-4-Real/arXiv_Daily/tree/main/src/run.sh): Script to run all.


## Run
```
# 1. environment preparation
>>> git clone https://github.com/Aman-4-Real/arXiv_Daily.git
>>> cd src && pip install -r requirements
```
```
# 2. define your own urls and keywords and modify 'src/configs.py'
```
```
# 3. test interface
>>> python main.py
```
```
# 4. set your paths at 'src/run.sh'
```
```
# 5. use crontab command to run periodically
>>> crontab -e
# add '0 8 * * * cd /YOUR_PATH/arxiv_daily/src/ && sh run.sh >> /YOUR_PATH/arxiv_daily/src/log' at the end to run at 8 a.m. evryday and save log
```
DONE & ENJOY!


## Demo

[www.aman.love:9002](http://www.aman.love:9002): for papers of NLG/Dialogue/Multimodality, update at around 0840(UTC+8) everyday.
