from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello():
    f=open("/var/www/html/black_lists/porno").read()
    return f

@app.errorhandler(404)
def page_not_found(e):
    return render_template('templates/404.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=8080)