import base64
from time import sleep
import local as conf
from reader import messages

assert conf.VK_IGNORE_LIST
assert conf.VK_AUTH

time = 5000

def get_api():
    decoded = [base64.b64decode(s).decode('utf-8') for s in conf.VK_AUTH]

    return messages(*decoded)

def endless_reader(api):
    while True:
        try:
            for id in conf.VK_IGNORE_LIST:
                api.method("messages.markAsRead", peer_id=id)
        except:
            pass

        sleep(time / 1000)


if __name__ == '__main__':
    vk_api = get_api()
    endless_reader(vk_api)
