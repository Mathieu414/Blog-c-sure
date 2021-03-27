#!/usr/bin/env python3
# coding: utf-8

from flask import Flask, g
from flask import abort, request, make_response
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    app.logger.debug('serving root URL /')
    return render_template('accueil.html')

@app.route('/Loup life')
def loup():
    app.logger.debug('Loup life')
    return render_template('Loup_cesure.html')

@app.route('/Nino life')
def nino():
    app.logger.debug('Nino life')
    return render_template('Nino_cesure.html')

@app.route('/Alexandre life')
def alexandre():
    app.logger.debug('Alexandre life')
    return render_template('Alexandre_echange.html')

@app.route('/SHN life')
def shn():
    app.logger.debug('SHN life')
    return render_template('SHN_CO.html')

@app.route('/new_post', methods = ["GET","POST"])
def new():
    app.logger.debug('New Post')
    if request.method == "GET" :
        username = request.args.get("username")
        password = request.args.get("password")
        if username == "avergnaud" and password == "motdepasse" :
            return render_template("new_post.html", user = username)
        if username == "avilanoba" and password == "motdepasse" :
            return render_template("new_post.html", user = username)
        if username == "mperrin" and password == "motdepasse" :
            return render_template("new_post.html", user = username)
        if username == "lpetitjean" and password == "motdepasse" :
            return render_template("new_post.html", user = username)
        if username == "nmolin" and password == "motdepasse" :
            return render_template("new_post.html", user = username)
    if request.method == "POST" :
        username = request.args.get("username")
        if request.form is not None :
            new_article = request.form.to_dict()
            if username == "avergnaud" :
                return render_template("SHN_CO.html", new_article = new_article) 
            if username == "avilanoba" :
                return render_template("Alexandre_echange.html", new_article = new_article) 
            if username == "mperrin" :
                return render_template("SHN_CO.html", new_article = new_article) 
            if username == "lpetitjean" :
                return render_template("Loup_cesure.html", new_article = new_article)
            if username == "nmolin" :
                return render_template("Nino_cesure.html", new_article = new_article) 
    return render_template('new_post.html')

# Script starts here
if __name__ == '__main__':
    from os import environ
    DEBUG = environ.get('DEBUG')
    app.run(port=8000, debug=DEBUG)

# VIM MODLINE
# vim: ai ts=4 sw=4 sts=4 expandtab fileencoding=utf8

"""
HELLO_STRINGS = {
        "cn": "你好世界\n",
        "du": "Hallo wereld\n",
        "en": "Hello world\n",
        "fr": "Bonjour monde\n",
        "de": "Hallo Welt\n",
        "gr": "γειά σου κόσμος\n",
        "it": "Ciao mondo\n",
        "jp": "こんにちは世界\n",
        "kr": "여보세요 세계\n",
        "pt": "Olá mundo\n",
        "ru": "Здравствуй, мир\n",
        "sp": "Hola mundo\n"
}

@app.route('/hello_world')
def hello_world():
    app.logger.debug('Hello world')
    app.logger.debug('Here is the request I got: {}'.format(request))
    app.logger.debug('Here is the headers I got: {}'.format([k for k in request.headers.keys()]))
    app.logger.debug('Here is the val I got: {}'.format([k for k in request.headers.values()]))

    r = request.headers['Accept-Language']
    app.logger.debug(r)
    if r in HELLO_STRINGS.keys():
        response = make_response(HELLO_STRINGS[r])
        response.headers['Content-Language'] = r
    else:
        response = make_response(HELLO_STRINGS['en'])
        response.headers['Content-Language'] = 'en'
   
    response.headers['Loup'] = 'Gentil'
    response.headers['Content-Type'] = 'text/plain'
    #abort(404)
    return response
    #return resp

@app.route('/about')
def about():
    from datetime import datetime
    today = datetime.today()
    app.logger.debug('about')
    # Create a context
    tpl_context = {}
    # Populate a context to feed the template
    # (cf. http://strftime.org/ for string formating with datetime)
    tpl_context.update({'day': '{:%A}'.format(today)})
    tpl_context.update({'d_o_month': '{:%d}'.format(today)})
    tpl_context.update({'month': '{:%B}'.format(today)})
    tpl_context.update({'time': '{:%X}'.format(today)})
    tpl_context.update({'date': today})
    # Now let's see how the context looks like
    app.logger.debug('About Context: {}'.format(tpl_context))
    return render_template('about.html', context=tpl_context, page_title="A propos")
"""