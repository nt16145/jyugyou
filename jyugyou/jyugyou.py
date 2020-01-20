# coding: utf-8
from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template, request

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')


@app.route('/')
def index():
    return render_template('jyugyou2.html')


@app.route('/<class_select>')
def class_select(class_select):
    # para = urllib.parse.urlparse(class_select).query
    f = request.args.get('f')
    s = request.args.get('s')
    res = requests.get(
        "http://jyugyou.tomakomai-ct.ac.jp/jyugyou.php?class=" +
        class_select)
    soup = BeautifulSoup(res.content)
    jyugyou = soup.find_all('td')
    leng = len(jyugyou)
    c = 0
    tr = 0
    after_jyugyou = []
    for i in range(100, leng):
        if (i + 1) != leng:
            j = i + 1
            jyugyou[j] = jyugyou[j].string
            if f == 'on' and 'フロンティアコース' in jyugyou[j]:
                c = 1
                continue
            if s == 'on' and '選択' in jyugyou[j] or '地球環境科学概論' in jyugyou[j]:
                c = 1
                continue
        if c == 1:
            c = 0
            continue
        if tr == 0:
            after_jyugyou.append('<tr><td>' + jyugyou[i].string + '</td>')
            tr = 1
        elif tr == 1:
            after_jyugyou.append('<td>' + jyugyou[i].string + '</td></tr>')
            tr = 0
    leng = len(after_jyugyou)
    return render_template("jyugyou.html", leng=leng, jyugyou=after_jyugyou)


if __name__ == "__main__":
    app.run( host='0.0.0.0', port=80)
