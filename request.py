import requests
from time import sleep


def send_message(msg, auth, url):

    payload = {
        'content': msg
    }

    header = {
        'authorization': auth
    }

    post = requests.post(url, data=payload, headers= header)
    p_json = post.json()
    id = p_json['id']
    return id


def del_message(ID, auth, url):

    header = {
        'authorization': auth
    }

    requests.delete(f'{url}/{ID}', headers = header)
    return 1


def send_and_del_msg(msg, auth, url):

    id = send_message(msg, auth, url)
    if id == 0:
        return 'Post Erro'
    else:
        pass
    sleep(0.5)
    delet = del_message(id, auth, url)
    if delet == 0:
        return 'Del Erro'
    else:
        pass
    return 'message is send, and, delete'


if __name__ == "__main__":
    msg = "YOUR MESSAGE"
    auth = "YOUR AUTHORIZATION CODE"
    url = 'CHAT URL'
    print(send_and_del_msg(msg,auth,url))






