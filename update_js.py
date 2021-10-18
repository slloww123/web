#coding=utf-8

from re import compile,search
from requests import get,codes
from bs4 import BeautifulSoup
# from IPython.display import HTML
from urllib.parse import unquote
from time import sleep,time

headers = {
  "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
}

while True:
  # movieffm
  #https://www.movieffm.net/cats/popular-movies/
  all = []
  for page_num in range(1,35+1):
    # Movieffm
    r = get('https://www.movieffm.net/cats/popular-movies/page/%d/'%(page_num))#, params = {'orderby':'view'})
    soup = BeautifulSoup(r.text, 'html.parser')
    # display(HTML(soup.prettify()))

    # movie detail link
    details = []
    for detail in soup.find_all('a',attrs={'href':compile('^https://www.movieffm.net/movies/.*/$')}):
      box_link = str(detail.get('href'))
      if box_link not in details:
        details.append(box_link)
    for detail in details:
      b = get(detail)
      box_soup = BeautifulSoup(b.text, 'html.parser')
      m3u8 = []
      line = box_soup.prettify().split('\n')
      for line in line:
        try:
          m3u8.append(unquote(search(r'=http.*m3u8',line).group()).replace('=',''))
        except:
          pass
      try:
        img = box_soup.select('div.sheader > div.poster > img[src]')[0]
        h1 = box_soup.select('div.sheader > div.data > h1')[0]
        if len(m3u8) > 0:
          info = {'title':h1.get_text(),'poster':img.get('src'),'m3u8':m3u8}
          all.append(info)
          print(info)
      except:
        pass
  with open('m3u8.js','w',encoding='utf-8') as f:
    f.write('m3u8 = \n%s'%str(all))





  # dict
  # https://ldwise.github.io/web/dict/vocas.md
  r = get('https://ldwise.github.io/web/dict/vocas.md', headers=headers)
  soup = BeautifulSoup(r.text, 'html.parser').prettify().replace('\r\n','')
  all = []
  for voca in soup.split('- '):
    v = get('https://dictionary.cambridge.org/dictionary/english-chinese-traditional/%s#caldcnt-1-1'%voca, headers=headers)
    soup = BeautifulSoup(v.text, 'html.parser')
    # display(HTML(soup.prettify()))
    outerhtml = ''
    try:
      outerhtml = soup.select('#page-content > div.pr.di.superentry > div.di-body > div > div')[0].prettify()
      all.append({'voca':voca,'html':outerhtml})
      print(voca)
    except:
      pass
  # soup.prettify()
  with open('vocas.js','w',encoding='utf-8') as f:
    f.write('vocas = \n%s'%str(all))
    
    
    
  start = time()
  print("Take an hour break")
  while (time()-start) <= 60*60:
    print("%.2f's waiting..."%float(time()-start),end='\r')
