import requests


def close_servers():

    try:
        requests.get('http://127.0.0.1:5000/stop_server')
        print('Servers closed!')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    close_servers()
