from flask import Flask
from flask import render_template
from flask import request
import time
app = Flask(__name__)


@app.route("/")
def hello():
    f=open("/var/www/html/black_lists/porno").read()
    return f

@app.route("/version")
def version():
    f_ver=open("/var/www/html/black_lists/version").read()
    return f_ver

@app.route("/test")
def test():
    return render_template('test.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/p", methods=['GET','POST'])
def panel():
    file_url = open("/var/www/html/black_lists/porno" , "r")
    url_list = file_url.read().splitlines()
    file_url.close()

    if request.method == 'POST':
        url = request.form['url']
        if not url in url_list:
            file_list_version = open("/var/www/html/black_lists/version" , "w")
            file_url = open("/var/www/html/black_lists/porno", "a")
            file_url.write(url+'\n')
            file_list_version.writelines(str(time.time()))
            file_url.close()
            file_list_version.close()

    return render_template('panel.html',messages= url_list)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=8080)