import os, sys
import requests
from urllib import parse
from bs4 import BeautifulSoup
import re


def savePageImages(url, imagespath='images'):
    def soupfindnSave(pagefolder, tag2find='img', inner='src'):
        if not os.path.exists(pagefolder): # create only once
            os.mkdir(pagefolder)
        for res in soup.findAll(tag2find):  
            if res.has_attr(inner): # check inner tag (file object) MUST exists
                try:
                    filename, ext = os.path.splitext(os.path.basename(res[inner])) # get name and extension
                    filename = re.sub('\W+', '', filename) + ext # clean special chars from name
                    fileurl = parse.urljoin(url, res.get(inner))
                    filepath = os.path.join(pagefolder, filename)
                    if not os.path.isfile(filepath): # was not downloaded
                        with open(filepath, 'wb') as file:
                            filebin = session.get(fileurl)
                            file.write(filebin.content)
                except Exception as exc:
                    print(exc, file=sys.stderr)   
    session = requests.Session()
    #... whatever other requests config you need here
    response = session.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    soupfindnSave(imagespath, 'img', 'src')

savePageImages('https://www.google.com', 'google_images')