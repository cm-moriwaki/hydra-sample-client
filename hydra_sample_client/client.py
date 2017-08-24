from flask import Flask, render_template, redirect, url_for, request, jsonify
import requests
from hydra.client import Client

app = Flask(__name__)
app.secret_key = 'client secret key'
app.config['SESSION_TYPE'] = 'filesystem'

STATE = "this is sample state ......"

HYDRA_URL = 'http://localhost:4444'
CLIENT_ID = 'some-consumer'
CLIENT_SECRET = 'consumer-secret'


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/run')
def run():
    scopes = request.args.get('scopes', 'pi').split(',')
    return redirect('{}/oauth2/auth?client_id={}&response_type={}&scope={}&state={}'.format(HYDRA_URL, CLIENT_ID, "code", ','.join(scopes), STATE))


@app.route('/callback')
def callback():
    print("@@@@@ callback...")
    error = request.args.get('error', None)
    error_description = request.args.get('error_description', None)
    if error:
        return render_template('home.html', error=error, error_description=error_description, callback=True)

    code = request.args.get('code', None)
    c = Client(HYDRA_URL, CLIENT_ID, CLIENT_SECRET)
    t = c.get_access_token(code)
    print("@@@@", t)
    token = t['access_token']
    return render_template('home.html', error=error, error_description=error_description, callback=True, code=code, token=token)


@app.route('/get_info')
def get_info():
    token = request.args.get("token")
    # IDPから情報を取得
    r = requests.get("http://localhost:65001/information_use_token", params=dict(token=token))
    if not r:
        return "無効なトークンのため情報取得失敗"
    data = r.json()
    return jsonify(data)


def cli():
    app.run(host="0.0.0.0", port=65002)


if __name__ == "__main__":
    cli()
