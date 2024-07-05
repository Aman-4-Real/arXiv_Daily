# -*- encoding: utf-8 -*-
'''
@Date     : 2021.09.10
@Author   : Aman
@Contact  : cq335955781@gmail.com
'''

import os

for _, dirs, files in os.walk("/home/caoqian/arxiv_daily/data/"):
    file_prefix = [eval(file.split('.')[0]) for file in files]
    file_prefix.sort()
    keep_files = [str(i)+'.json' for i in file_prefix[-7:]]
    for file in files:
        if file not in keep_files:
            os.remove("/home/caoqian/arxiv_daily/data/" + file)
    print("Keep latest files in last 7 days:", keep_files)
print("="*20)


