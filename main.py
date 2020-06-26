import requests
from bs4 import BeautifulSoup
import json

res = requests.get('https://g1.globo.com/')
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text, 'html.parser')

posts = soup.find_all(class_ = 'feed-post bstn-item-shape type-materia')

all_posts = []

for post in posts:
    try:
        title = post.find(class_ = 'feed-post-header-chapeu').text
        div_link = post.find(class_ = 'feed-post-body-title gui-color-primary gui-color-hover')
        a_link = div_link.a
        link_title = a_link.text
        link_href = a_link['href']
        resumo = post.find(class_ = 'feed-post-body-resumo').text
        
        all_posts.append({
            'title': title,
            'linkTitle': link_title,
            'linkHref': link_href,
            'resumo': resumo
        })
    except AttributeError:
        pass

print(all_posts)

with open('posts.json', 'w') as json_file:
    json.dump(all_posts, json_file, indent=3, ensure_ascii=False)