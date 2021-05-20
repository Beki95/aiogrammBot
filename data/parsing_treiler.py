# import requests
# from bs4 import BeautifulSoup as BS
#
#
# def parse_tg(url):
#     response = requests.get(url)
#
#     soup = BS(response.content, "lxml")
#     text = soup.find_all("a", class_="tgme_widget_message_inline_button url_button")
#     frames = soup.find_all("a", class_="tgme_widget_message_photo_wrap")
#     for i in text:
#         print(i.get("href"))
#     for frame in frames:
#         img = frame.get("style").split()
#         print(img[0][34:-2])
#
#
# url = "https://t.me/s/films555kino"
# parse_tg(url)
