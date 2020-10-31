import base64
import json
import math
import os
import datetime
from time import sleep
import local as conf
from reader import messages

VK_AUTH = [os.getenv('VK_USERNAME'), os.getenv('VK_PASSWORD')]
VK_IGNORE_LIST = json.loads(os.getenv('VK_IGNORE_LIST'))

def get_delay() -> float:
    now = datetime.datetime.now()
    x = now.hour + now.minute / 60

    c_1 = 420
    c_2 = 5000
    k = 17.4

    return (-1 / (1 + math.exp(k - 1.1 * x)) * (c_2 - c_1) + c_2) / 1000

def get_api():
    decoded = [base64.b64decode(s).decode('utf-8') for s in conf.VK_AUTH]
    return messages(*decoded)

def write_to_file(data):
    with open(f'debug.txt', 'a') as f:
        f.write(json.dumps(data) + '\n')

def endless_reader(api):
    catch_error = 0
    e = None
    while True:
        try:
            for id in conf.VK_IGNORE_LIST:
                resp = api.method("messages.markAsRead", peer_id=id)
                write_to_file(resp)
                catch_error = 0
        except:
            catch_error += 1
            pass
        if catch_error > 3:
            description = 'No information'
            if e is not None:
                description = f'Exception:\n{str(e)}'

            write_to_file(description)
            break

        sleep(get_delay())

if __name__ == '__main__':
    vk_api = get_api()
    endless_reader(vk_api)
