
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
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/p", methods=['GET','POST'])
def panel():
    f_url_porn = open("/var/www/html/black_lists/porno" , 'r')
    f_url_anonum = open("/var/www/html/black_lists/anonymizer" ,'r')
    f_url_banner = open("/var/www/html/black_lists/banners", 'r')
    f_url_bl_all = open("/var/www/html/black_lists/block_all", 'r')
    f_url_video = open("/var/www/html/black_lists/video_hosting", 'r')
    f_url_soc_net = open("/var/www/html/black_lists/social_networks", 'r')
    url_list_porn = f_url_porn.read().splitlines()
    url_list_anonum = f_url_anonum.read().splitlines()
    url_list_banner = f_url_banner.read().splitlines()
    url_list_bl_all = f_url_bl_all.read().splitlines()
    url_list_video = f_url_video.read().splitlines()
    url_list_soc_net = f_url_soc_net.read().splitlines()


    f_url_porn.close()

    if request.method == 'POST':
        url = request.form['url']
        url = url.strip()

        if not url in url_list_porn:
            file_list_version = open("/var/www/html/black_lists/version", "w")
            file_list_version.writelines(str(time.time()))
            file_list_version.close()

            f_url_porn = open("/var/www/html/black_lists/porno", "a")
            f_url_porn.write(url + '\n')
            f_url_porn.close()

        return render_template('panel.html',porn_links= url_list_porn,soc_net_links=url_list_soc_net,err=1)

    return render_template('panel.html',porn_links= url_list_porn,soc_net_links=url_list_soc_net)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=8080)