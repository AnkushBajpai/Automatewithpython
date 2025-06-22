#! python3
# searchpypi.py  - Opens several search results.

import requests, sys, webbrowser, bs4, logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)

print('Searching...')    # display text while downloading the search result page
headers = {
   'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}
res = requests.get('https://pypi.org/search/?q='+' '.join(sys.argv[1:]), headers=headers)
res.raise_for_status()

logging.debug(res.text)
# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result.
linkElems = soup.select('.package-snippet')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)