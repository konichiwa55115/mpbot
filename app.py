#Thank you LazyDeveloper for helping me in this journey !
#Must Subscribe On YouTube @LazyDeveloperr 
from werkzeug.urls import url_quote
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '@LazyDeveloper'


if __name__ == "__main__":
    app.run()
