from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def hello():
    f=open("/var/www/html/black_lists/porno").read()
    return f
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
    print(type(url_list))
    file_url.close()
    temp='mirporno.net'
    print (type(temp))
    print(temp in url_list)

    #print (str(type(f)))

    if request.method == 'POST':
        url = request.form['url']
        print("type url ",type(url))
        print(url_list)
        if not url in url_list:
            file_url = open("/var/www/html/black_lists/porno", "a")
            file_url.write(url+'\n')
            print(url)
            file_url.close()
        else:
            print('false')

    return render_template('panel.html',messages= url_list)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=8080)