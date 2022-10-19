from urllib import response
from flask import *
import requests

app = Flask(__name__)

def get_meme():
    url = 'https://meme-api.herokuapp.com/gimme'
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    return meme_large

@app.route("/")
def index():
    meme_pic = get_meme()
    return render_template('index.html', meme_pic=meme_pic)

if __name__=='__main__':
    app.run()