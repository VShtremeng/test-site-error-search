# import time
# from datetime import time
from time import sleep
import asyncio
import aiohttp
from aiohttp import web
import json
import requests
import telebot
from selenium.webdriver.chrome.webdriver import WebDriver
from flask import Flask
# from selenium.webdriver.remote.webelement import WebElement
# from telegram import Bot
# from telegram.ext import Updater
# from telegram.ext import CommandHandler
# from telegram.ext import MessageHandler
# from telegram.ext import Filters
# from telegram.ext import MessageHandler
# from echo.config import TG_TOKEN

# def test_site_error_search():
#     start: int
#     for start in range(3):
#         driver: WebDriver = WebDriver(executable_path='C://selenium//chromedriver.exe')
#         driver.get('https://delikateska.ru/?utm_source=test_200')
#         assert driver.title == 'Интернет магазин продуктов и деликатесов — купить продукты онлайн с доставкой на дом'
#         r = requests.get('https://delikateska.ru/?utm_source=test_200')
#         print(r.status_code)
#         print(r.headers['content-type'])
#         # time.sleep(15)
#         sleep(15)
#         driver.close()
#         # if r.status_code == 200:
#             # r = open('report.txt', 'w')
#             # r.write('The test was successful! Code 200.')
#             # r.close()
#
#         # else:
#         bot = telebot.TeleBot(TOKEN = "951117144:AAE3xB1Xo9a0JUfaVD-q9qXYQsr1CkPZTzk")
#         API_URL = 'https://api.telegram.org/bots951117144:AAE3xB1Xo9a0JUfaVD-q9qXYQsr1CkPZTzk/sendMessage'
#
#         async def handler(request):
#             data = await request.json()
#             headers = {'Content-Type': 'application/json'}
#             message = {
#                 'chat_id': data['message']['chat']['id'],
#                 'text': data['message']['text']
#             }
#             async with aiohttp.ClientSession(loop=loop) as session:
#                 async with session.post(API_URL,
#                                         data=json.dumps(message),
#                                         headers=headers) as resp:
#                     try:
#                         assert resp.status == 200
#                     except:
#                         return web.Response(status=500)
#             return app
#
#         async def init_app(loop):
#             app = web.Application(loop=loop, middlewares=[])
#             app.router.add_post('/api/v1', handler)
#             return app
#         if __name__ == '__main__':
#             loop = asyncio.get_event_loop()
#             try:
#                 app = loop.run_until_complete(init_app(loop))
#                 web.run_app(app, host='0.0.0.0', port=23456)
#             except Exception as e:
#                 print('Error create server: %r' %e)
#             finally:
#                 pass
#             loop.close()
        # def get_updates_json(request):
        #     response = requests.get(request + 'getUpdates')
        #     return response.json()
        # def last_update(data):
        #     results = data['result']
        #     total_updates = len(results) - 1
        #     return results[total_updates]
        # def get_chat_id(update):
        #     chat_id = update['message']['chat']['id']
        #     return chat_id
        # def send_mess(chat, text):
        #     params = {'chat_id': chat, 'text': text}
        #     response = requests.post(url + 'sendMessage', data=params)
        #     return response
        # chat_id = get_chat_id(last_update(get_updates_json(url)))
        # send_mess(chat_id, 'The test was successful! Code 200.')
        #
        # def main():
        #     update_id = last_update(get_updates_json(url))['update_id']
        #     while True:
        #         if update_id == last_update(get_updates_json(url))['update_id']:
        #             send_mess(get_chat_id(last_update(get_updates_json(url))), 'test')
        #             sleep(1)
        # if __name__ == '__main__':
        #
        #     main()
        # for message in r.json()['result']:
        #     last = int(message['update_id'])
        #     requests.post('https://delikateska.ru/?utm_source=test_200',
        #                     data=json.dumps(message),
        #                     headers={'Content-type': 'application/json',
        #                                 'Accept': 'text/plain'}
        #                     )
        #     logging.warning('FAIL' + r.text)
# TOKEN = '731470740:AAF-invdaiIFBLxfbn46_-N-6kPO5l4MDZ0'
# MAIN_URL = f'https://api.telegram.org/bot{TOKEN}/getME'
#
# r = requests.get(f'{MAIN_URL}/getME')
#
# print(r.json())
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Test flask app</h1>'

if __name__ == '__test_site_error_search':
    app.run()


