#!/usr/bin/python
import requests
from re import findall
from time import sleep

def download_image(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        print('Downloading %s...' % (file_name))

    with open('/Users/alexzoltowski/Documents/Backgrounds/' + file_name, 'wb') as fo:
        for chunk in response.iter_content(4096):
            fo.write(chunk)


page_source = []

while len(page_source) == 0:
    sleep(1)
    page_source = requests.get('https://reddit.com/r/wallpapers').text.split(' ')
                                                    #filtering uneeded source
    page_source = [str(link) for link in page_source if 'imgur' in link and 'data-href-url' not in link\
                                                    and 'href' in link and 'quot' not in link and\
                                                    'domain' not in link]

    page_source = [findall(r'([^"]*)', link)[2] for link in page_source]

links = []

for link in page_source:
    if link not in links:
        links.append(link)

for index, link in enumerate(links):
    download_image(link + '.jpg', str(index) + '.jpg')
