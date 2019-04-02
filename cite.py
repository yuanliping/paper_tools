import requests

import os
import re
import time
import random
from stem import Signal
from stem.control import Controller
import requests

TOR_PORT = 9050
CONTROL_PORT = 9051
TOR_PASSWORD = 'mypassword'

PAPER_DIR = '../acl_2016/'
available_url = [
    'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q='
]

proxy = '127.0.0.1:%d' % TOR_PORT
proxies = {
    'http': 'socks5://' + proxy,
    'https': 'socks5://' + proxy,
}


class TorControl():
    def __init__(self):
        self.controller = Controller.from_port(port=CONTROL_PORT)
        self.controller.authenticate(TOR_PASSWORD)

    def renew_tor(self):
        self.controller.signal(Signal.NEWNYM)


tc = TorControl()

file_names = []
check_cite = re.compile('\d+_cited_')
for root, dirs, files in os.walk(PAPER_DIR):
    for file in files:
        if re.search(check_cite, file):
            continue
        file_name = file.split('.')[0]
        file_names.append(file_name)

pattern = re.compile('Cited by (\d+)')
for file_name in file_names:
    time.sleep(2)
    tc.renew_tor()
    # print(requests.get("http://ipecho.net/plain", proxies=proxies).text)
    try:
        url = random.choice(available_url) + file_name.replace(' ', '+')
        html = requests.get(url, proxies=proxies)
        search = re.search(pattern, html.text)

        cite_num = search.group(1)
        print('renaming: %s %s' % (cite_num, file_name))
        os.rename('%s%s.pdf' % (PAPER_DIR, file_name), '%s%s_cited_%s.pdf' % (PAPER_DIR, cite_num, file_name))
    except Exception as err:
        print('error occurs when renaming %s' % file_name)
        continue
