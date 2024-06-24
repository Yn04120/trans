import requests
from bs4 import BeautifulSoup
# from fake_useragent import UserAgent

def read(word):
#     ua = UserAgent()
#     user_agent = ua.random
#     headers = {'user-agent': user_agent}
    url = f'https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/{word}'
    user_agent = {'user-agent': 'Mozilla/5.0'}
    html = requests.get(url, headers=user_agent)
#     html = requests.get(url, headers=headers)
    html.encoding = 'utf-8'
    bs = BeautifulSoup(html.content, 'html.parser')
    data = bs.find_all('span', class_="dtrans")[0]
    translation = data.text
    try:
        english = bs.find_all('span', class_="hw dhw")[0].text
        return f'{english} => {translation}'
    except:
        return '查無此字' 