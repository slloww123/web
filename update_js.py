#coding=utf-8

from re import compile,search
from requests import get,codes
from bs4 import BeautifulSoup
# from IPython.display import HTML
from urllib.parse import unquote
# from time import sleep,time
from random import randint

USER_AGENTS = [
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
 "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
 "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
 "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
 "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
 "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
 "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527&#43; (KHTML, like Gecko, Safari/419.3) Arora/0.6",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
 "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
 "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
random_agent = USER_AGENTS[randint(0, len(USER_AGENTS)-1)]
headers = {
    "User-Agent":random_agent,
  }

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
# start = time()
# while (time()-start) <= 1800:
#   print("%s's waiting..."%str(time()-start),end='\r')





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
