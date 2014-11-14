#!/usr/bin/env python
"""
Pull out the title and body text of a nytimes article given its url.
Write it to a file.
"""
import urllib2
from bs4 import BeautifulSoup
from cookielib import CookieJar
#import re

def soup(url_str):
    """ Turns a url into soup. CookieJar handles the http sesson."""
    cookie = CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    page = opener.open(url_str)
    html = page.read()
    return BeautifulSoup(html,'html.parser')

def pop_ny(article_title):
    """ Removes ' - NYTimes.com' from title """
    tlist = article_title.split(" ")
    tout = " ".join(tlist[0:len(tlist)-2])
    return tout

#def detag(str_text):
#    """ Removes html tags from string. """
#    return re.sub("<.*?>", "\n", str_text)

def get_title(soup_obj):
    """ Gets the title from bs4 object and removes ' - NYTimes.com' """  
    t = soup_obj.title.string
    tlist = t.split(" ")
    tout = " ".join(tlist[0:len(tlist)-2])
    return tout

def get_body(soup_obj):
    """ Gets the body of a bs4 objectification of a nytimes article
    and returns it as a single string."""
    body = soup_obj.find_all("p",class_="story-body-text") 
    l = []
    for bit in body:
        l.append(' '.join(bit.stripped_strings))
    bout = "\n".join(l)
    return bout

if __name__ == '__main__':
    add = raw_input("Enter the URL of the NYTimes article to parse: ")
    dest = raw_input("Thanks. Enter the name of the output file: ")
    broth = soup(add)
    tout = get_title(broth).encode("utf-8")
    bout = get_body(broth).encode("utf-8")
    f = open(dest,"w+")
    f.write("title:\n {} \n\n body:\n {}".format(tout,bout))
    f.close()
