import requests
from bs4 import BeautifulSoup as BS
import asyncio
import aiohttp

from utils.db_api.postgres import Database


# async def parsing(url):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
#                       " Chrome/84.0.4147.135 YaBrowser/20.8.3.115 Yowser/2.5 Safari/537.36"
#     }
#     response = requests.get(url, headers=headers, cookies={"mos_id": 'CllGx1yOW5nBYizxkxtbAgA=;'})
#     soup = BS(response.text, "lxml")
#     text = soup.find_all("div", class_="all_anime_global")
#     result = []
#     pk = 1
#     for i in text:
#         name = " ".join(i.find("span", class_="the_invis").text.split()[1:]).lower()
#         # result.append(i.find("span", class_="the_invis").text)
#         link = "https://jut.su/" + i.find("a").get("href")
#         # result.append("https://jut.su/" + i.find("a").get("href"))
#         photo = i.find("div", class_="all_anime_image").get("style").split("url")[1].split("no-repeat;")[0][2:-4]
#         print(name, link, "  ", photo)
#
#         await db.insert_into(pk, str(name), str(link), str(photo), "kinos")
#         pk += 1
    # return result


# url = "https://jut.su/anime/"
# # print(parsing(url))
# loop = asyncio.get_event_loop()
# db = Database(loop)
# loop.run_until_complete(parsing(url))

# асинхронный парсер. сайт animevost
# создаем функцию для получения url и ответа html.text()
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            return html


# функция для парсинга title
async def title_link(text):
    list_title = []
    for i in text:
        title = i.find("a").text
        list_title.append(title)
    return list_title


# функция для parse принимает html и парсит страницу
async def parse(html):
    soup = BS(html, "lxml")
    title = soup.find_all("div", class_="shortstoryHead")
    title = await title_link(title)
    return title


# главная функция упорядочность действий
async def main(url):
    html = await fetch(url)
    text = await parse(html)
    return text


# func запуска в асинхронном потоке
async def run(urls):
    return await asyncio.gather(*[main(url) for url in urls])

# a = 1
# end = 20
# for i in range(3):
#     urls = [f"https://animevost.am/page/{num}/" for num in range(a, end+1)]  # лучше парсить по 20 страниц за раз
#     print(urls)
#     # асинхронный запуск
#     loop = asyncio.get_event_loop()
#     l = loop.run_until_complete(run(urls))
#     print(l)
#     print(l.count([]))
#     a += 20
#     end += 20


