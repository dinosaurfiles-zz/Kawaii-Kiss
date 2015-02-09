#!/usr/bin/python
import httplib2
from BeautifulSoup import BeautifulSoup
import urllib2
import cookielib
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

# if link given is not from a single page. try download all episodes


def getlinks(url):  # get links for each anime episode
    hdr = {'User-Agent':
           'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0'}
    re = urllib2.Request(url, headers=hdr)
    html_page = urllib2.urlopen(re)
    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a'):
        if fnmatch(link.get('href'), '/Anime/*'):
            print link.get('href')

# dis func refers to the quality of the files and its links


def getvideosingle(url):
    hdr = {'User-Agent':
           'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0'}
    re = urllib2.Request(url, headers=hdr)
    html_page = urllib2.urlopen(re)
    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a'):  # get link of videos
        if fnmatch(link.get('href'), "https://redirector.googlevideo.com/*"):

            # this block gets the video quality and filetype
            hh = str(link)
            spp = hh.rsplit('>')[-2]
            print '\nquality ' + spp.rsplit('<')[0]
            print link.get('href')

# dis func gets the original name of the Anime


def getfilename(url):
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [
        ('User-Agent',
         'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0')]

    urllib2.install_opener(opener)
    usock = urllib2.urlopen(url)
    data = usock.read()
    usock.close()

    data = data.split('\n')
    print data[(data.index('<b>Filename:</b>')) + 1]

if __name__ == "__main__":
    # main(sys.argv[1:])
    url = "http://kissanime.com/Anime/Sakura-Trick/Episode-001?id=62116"
    # getlinks(url)
    getvideosingle(url)
    # getfilename(url)
    # getHTMLsource("http://kissanime.com/Anime/Sakura-Trick")
