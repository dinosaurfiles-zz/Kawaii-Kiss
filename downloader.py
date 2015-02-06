#!/usr/bin/python
import httplib2
from BeautifulSoup import BeautifulSoup, SoupStrainer
import urllib2
import cookielib
import re
from fnmatch import fnmatch, fnmatchcase


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print 'Input file is "', inputfile
    print 'Output file is "', outputfile


def getlinks(url):  # get links for anime page
    hdr = {'User-Agent':
           'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0'}
    re = urllib2.Request(url, headers=hdr)
    html_page = urllib2.urlopen(re)
    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a'):
        if fnmatch(link.get('href'), '/Anime/*'):
            print link.get('href')


def getvideosingle(url):
    hdr = {'User-Agent':
           'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0'}
    re = urllib2.Request(url, headers=hdr)
    html_page = urllib2.urlopen(re)
    soup = BeautifulSoup(html_page)

    for link in soup.findAll('a'):
        if fnmatch(link.get('href'), "https://redirector.googlevideo.com/*"):
            hh = link(None)
            print hh
            print link.get('href')

if __name__ == "__main__":
    # main(sys.argv[1:])
    #url = "http://kissanime.com/Anime/Sakura-Trick/"
    url = "http://kissanime.com/Anime/Sakura-Trick/Episode-001?id=62116"
    # getlinks(url)
    getvideosingle(url)
    # getHTMLsource("http://kissanime.com/Anime/Sakura-Trick")
