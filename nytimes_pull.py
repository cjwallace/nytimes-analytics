#!/usr/bin/env python
# encoding: utf-8
"""
nytimes_pull.py

Created by Hilary Mason on 2011-02-17.
Copyright (c) 2011 Hilary Mason. All rights reserved.

A tiny modification made by Chris J. Wallace on 2014-03-23 to allow use of 
nytimes article search API v2.

"""

import urllib
import json
import sys

def main(api_key, category, label):

    content = []
    for i in range(0,1):
        h = urllib.urlopen("http://api.nytimes.com/svc/search/v2/articlesearch.json?[fq=news_desk:(%s)]&api-key=%s&offset=%s" % (category, api_key, i))
        data = json.loads(h.read())
        for result in data['response']['docs']:
            content.append(result['web_url'])

    f = open(label, 'w')
    for line in content:
        f.write('%s\n' % line)
        ##.encode('utf-8')
    f.close()

if __name__ == '__main__':
    cat = sys.argv[1]
    lab = sys.argv[2]
    key = "a0ae4cc5eb28482c56e3147071ab5969:14:69032440"
    main(key,cat,lab)

## "[Top/News/Sports]"
## "[Top/Features/Arts]"
