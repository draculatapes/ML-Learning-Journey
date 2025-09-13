'''
Web scraping often involves making numerous network requests to fetch web pages. These tasks are I/O bound because they spend a significant amount of time waiting for responses from the server. Multithreading can significantly improve performance by allowing multiple web pages to be fetched concurrently. If there are multiple web pages, we can create that many threads and fetch all the content in parallel.
'''

'''
https://python.langchain.com/docs/concepts/
https://python.langchain.com/docs/tutorials/
https://python.langchain.com/docs/introduction/
'''
import threading
import requests

from bs4 import BeautifulSoup

urls=[
    'https://python.langchain.com/docs/concepts/',
'https://python.langchain.com/docs/tutorials/',
'https://python.langchain.com/docs/introduction/'
]


def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')
threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
print('all pages are scraped ! ')
