import json
import os

import requests
from auth_data import token


def main():
    group_name = 'baneks'
    url = f'https://api.vk.com/method/wall.get?domain={group_name}&count=100&access_token={token}&v=5.131'
    src = requests.get(url).json()
    posts = src['response']['items']
    apr_posts = []

    if os.path.exists(group_name):
        print(f'Директория с {group_name} уже существует!')
    else:
        os.mkdir(group_name)

    for post in posts:
        if 'attachments' in post:
            attach = set()

            for att in post['attachments']:
                attach.add(att['type'])

            if {'photo'} == attach:
                flag = True

                for att in post['attachments']:
                    link = att['photo']['sizes'][-1]['url']
                    if not link.startswith('https://sun'):
                        flag = False

                if flag:
                    apr_posts.append([])

                    apr_posts[-1].append(post['text'])
                    for att in post['attachments']:
                        link = att['photo']['sizes'][-1]['url']
                        apr_posts[-1].append(link)

        elif 'copy_history' not in post:
            apr_posts.append(post['text'])

    [print(x, '\n') for x in apr_posts]
    with open(f'{group_name}/{group_name}.json', 'w', encoding='UTF-8') as f:
        json.dump(posts, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
