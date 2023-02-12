from flask import Flask
from tasks import hello

app = Flask(__name__)

@app.route("/")
def index():
    hello.delay()
    return 'OK!'

if __name__ == '__main__':
    app.run()
