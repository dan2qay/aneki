import json
import os

import requests
from auth_data import token

import pickle


def censor():
    with open('data/censor.pkl', 'rb') as f:
        a = pickle.load(f)
    return a


def get_100_posts(offset):
    group_name = 'baneks'
    url = f'https://api.vk.com/method/wall.get'

    src = requests.get(url,
                       params={
                           'domain': group_name,
                           'count': 100,
                           'access_token': token,
                           'v': 5.131,
                           'offset': offset
                       }).json()
    return src


def find_all(a_str, sub):
    start = 0
    ids = []
    if a_str.find(sub) == -1:
        return -1
    else:
        while True:
            start = a_str.find(sub, start)
            if start == -1:
                return ids
            else:
                ids.append(start)
            start += len(sub)


def main():
    COUNTER = 0
    offset = 0
    group_name = 'baneks'
    attempt = 0
    cnsr = censor()

    while COUNTER < 2600:
        print(f'Количество анекдотов: {COUNTER}')
        try:
            src = get_100_posts(offset)
            posts = src['response']['items']
        except:
            if attempt >= 5:
                break
            else:
                attempt += 1
                continue

        attempt = 0
        apr_posts = []

        for post in posts:
            if 'copy_history' not in post and 'attachments' not in post:
                text = post['text']
                text_lower = text.lower()
                for mat in cnsr:
                    f = find_all(text_lower, mat)
                    if f != -1:
                        for idx in f:
                            text = text[:idx + 1] + '*' + text[idx + 2:]

                apr_posts.append(str(COUNTER) + ') ' + text)
                COUNTER += 1

        with open(f'{group_name}/{group_name}.txt', 'a', encoding='UTF-8') as f:
            for anek in apr_posts:
                # print(anek)
                f.write(anek)
                f.write('\n')

        offset += 100


if __name__ == '__main__':
    main()
