from flask import Flask, render_template
from emails import Pfp




# print(image_url[1])
app = Flask(__name__)

@app.route("/")
def home():
    img = Pfp()

    image_url = img.fetch_image().split('"')

    return  render_template("index.html" , url = image_url[1])


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)