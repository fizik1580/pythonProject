from flask import Flask
from datetime import timedelta
from flask import session, app
import time
import random

app = Flask(__name__)

'''
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(second=3)
'''
@app.route('/', methods=['POST', 'GET'])
#
def hello():
    sleep_time = random.randrange(400, 600)
    sleep_time: float = sleep_time/1000.0
    time.sleep(sleep_time)
    print(sleep_time)

    return 'Hello, World!'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
