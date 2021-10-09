#coding=utf-8
#https://www.movieffm.net/cats/popular-movies/

from re import compile,search
from requests import get,codes
from bs4 import BeautifulSoup
# from IPython.display import HTML
from urllib.parse import unquote
from time import sleep

while True:
  all = []
  for page_num in range(1,35+1):
    # Movieffm
    r = get('https://www.movieffm.net/cats/popular-movies/page/%d/'%(page_num), params = {'orderby':'view'})
    soup = BeautifulSoup(r.text, 'html.parser')
    # display(HTML(soup.prettify()))

    # movie detail link
    details = []
    for detail in soup.find_all('a',attrs={'href':compile('^https://www.movieffm.net/movies/.*/$')}):
      box_link = str(detail.get('href'))
      if box_link not in details:
        details.append(box_link)
    for detail in details:
      b=get(detail)
      box_soup = BeautifulSoup(b.text, 'html.parser')
      m3u8 = []
      line = box_soup.prettify().split('\n')
      for line in line:
        try:
          m3u8.append(unquote(search(r'=http.*m3u8',line).group()).replace('=',''))
          info = {'title':box_soup.find('title').get_text().replace(' - Movieffm電影線上看',''),'m3u8':m3u8}
          print(info['title'],info['m3u8'])
          all.append(info)
        except:
          pass
  with open('m3u8.js','w',encoding='utf-8') as f:
    f.write('m3u8 = \n',str(all))
  sleep(3600)
