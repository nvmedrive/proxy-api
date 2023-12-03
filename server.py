from flask import Flask, request, Response

app = Flask(__name__)

def get_credentials():
    credentials = {}
    with open('auth.txt', 'r') as file:
        for line in file:
            user, password = line.strip().split(':')
            credentials[user] = password
    return credentials

def authenticate_user(username, password):
    credentials = get_credentials()
    return credentials.get(username) == password

def get_proxies(proxy_type):
    filename = f'checker/{proxy_type.lower()}.txt'
    with open(filename, 'r') as file:
        proxies = file.read()
    return proxies

@app.route('/api', methods=['GET'])
def api():
    username = request.args.get('user')
    password = request.args.get('pass')
    proxy_type = request.args.get('type')

    if not authenticate_user(username, password):
        return 'Invalid credentials', 401

    if proxy_type not in ['HTTP', 'SOCKS4', 'SOCKS5']:
        return 'Invalid proxy type', 400

    proxies = get_proxies(proxy_type)

    return Response(proxies, content_type='text/plain')
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
