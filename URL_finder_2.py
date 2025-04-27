import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

def extraxt_urls(response, base_url):
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a')

        absolute_urls = set()
        for link in links:
            href = link.get('href')
            if href and not href.startswith('mailto:') and not href.startswith('tel:'):
                absolute_url = urljoin(base_url, href)
                absolute_urls.add(absolute_url)

        print(list(absolute_urls))

    if response.status_code == 404:
        print(404)
    else:
        print(response.status_code)

def get_absolute_links(base_url):
    while True:
        #try:
            response = requests.get(base_url)
            print(extraxt_urls(response, base_url))
        #except:
        #    print("Fehler")
        #print("schlaf 1")
        #time.sleep(1)

url = 'https://beispiel.de/'
links = get_absolute_links(url)
print("ende")
