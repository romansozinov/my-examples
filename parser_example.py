import requests
from bs4 import BeautifulSoup
import time
import csv
 
#получаем ссылки со страницы
#открываем каждую ссылку
#читаем страницу и сохраняем данные (заголовок, картинку, дату, описание, текст)
 
def get_html(url):
    user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get(url, headers=user_agent)
    return r.text
 
 
def get_items_list(html):
    """ Получение ссылок на статьи
    """
    soup = BeautifulSoup(html, 'lxml')
    items_page = soup.find('div', {'class':'post-entry'})
    
    pre_url = 'http://site.ru'
    items_list = []
    for link in items_page.find_all('a', href=True):
        a = link['href']
        items_list.append(pre_url + a)
        time.sleep(1)   
    return items_list
 
 
def get_clear_text(html):
    for l in html:
        l = str(l)
        l = l.replace('\n',' ')
        l = l.replace(' align=""center""','')
        l = l.replace('""','"')
        l = l.replace('<div class='post-entry">','')
        l = l.replace('&gt','')
        l=l.replace('&lt','')
        l=l.replace(';',' ')        
 
 
def get_item_data(link):
    soup = BeautifulSoup(get_html(link), 'lxml')
    item_data = []
    try:
        title = soup.find('h1').text.strip()
        item_data.append(title)
    except:
        title = 'Без заголовка'
    
    try:
        pre = 'http://site.ru'
        img = soup.find('div', class_='post-entry').img['src']
        item_data.append(pre+img)
    except:
        img = 'http://site.ru/images/no_image.jpg'
    
    try:
        html = soup.find('div', class_='post-entry')
        text = get_clear_text(html)
        item_data.append(text)
    except:
        text = 'Текст не найден'    
    
    return item_data
    
 
def main():
    url = 'http://site.ru/'
    path = '/home/user/csv/data.csv'
    
    html = get_html(url)
    counter = 1
    for link in get_items_list(html):
        data = get_item_data(link)
        with open(path, 'a', newline='') as csvfile:
            w = csv.writer(csvfile)
            w.writerow(data)
        print('Статья', counter)
        counter += 1
        time.sleep(2)
 
 
if __name__ == '__main__':
    main()