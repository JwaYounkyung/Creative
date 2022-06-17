import requests
import threading
import pandas as pd

from bs4 import BeautifulSoup as bs

def crawl(cate):
    total = []
    base = 'https://ling.auf.net/'
    'https://ling.auf.net/lingbuzz/_listing?community=Phonology&start=31'
    print(cate)
    print()
    start = 1
    while True:
        base_url = base + "lingbuzz/_listing?community=" + cate + "&start=" + str(start)
        res = requests.get(base_url)
        html = bs(res.text, 'html.parser')

        tables = html.select('table')
        temp_table = tables[2]
        paper_table = temp_table.select_one('table')
        if len(paper_table.text.strip()) == 0:
            break

        rows = paper_table.select('tr')

        for row in rows:
            paper = {}

            detail_url = row.select('td')[-1].select_one("a")['href']
            try:
                detail_page = requests.get(base + detail_url)
            except:
                break
            detail_page_html = bs(detail_page.text, 'html.parser')

            title = detail_page_html.select_one("center").font.extract().text
            print(cate, len(total), title)
            
            author_list = detail_page_html.select("center a")

            author = ''
            for person in author_list:
                author += person.text + ', '
            author = author.strip(', ')
            
            detail_page_html.center.decompose()
            detail_page_html.title.decompose()
            detail_page_html.table.decompose()
            detail_page_html.table.decompose()
            detail_page_html.p.decompose()

            abstract = detail_page_html.text.replace('’',"'").replace('“','"').replace("혻혻","").replace("/*<![CDATA[*/function onLoad(){};/*]]>*/", "").replace('”', '"').replace("—","-").replace("‘","'").replace("/n"," ").strip()
            
            paper['sentence'] = abstract
            paper['label'] = 0
            total.append(paper)

        if start == 1:
            start += 30
        else:
            start += 100
    
    data = pd.DataFrame(total)
    data.to_csv("Outcome3/data/" + cate + ".csv", encoding='utf-16', index=False)

category = ['morphology']

thread_count = len(category)
threads = []

for i in range(thread_count):
    thread = threading.Thread(target=crawl, args=( (category[i], ) ))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()