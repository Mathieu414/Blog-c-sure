#!/usr/bin/env python3
# coding: utf-8

from flask import Flask, g
from flask import abort, request, make_response
from flask import render_template
import glob
import os

app = Flask(__name__)

# Listes des articles par page contenus dans des dictionnaires
path_articles = str(os.getcwd())
list_path_Alex = glob.glob(str(path_articles+"/Alex/*.txt"))
list_path_Loup = glob.glob(str(path_articles+"/Loup/*.txt"))
list_path_Nino = glob.glob(str(path_articles+"/Nino/*.txt"))
list_path_SHN = glob.glob(str(path_articles+"/SHN/*.txt"))
list_articles_Alex = []
list_articles_Loup = []
list_articles_Nino = []
list_articles_SHN = []

def create_dict(path) :
    with open(path, "r") as fichier :
        lines = fichier.readlines()
        return {"title" : lines[0], "news" : '\n'.join(lines[1:])}

@app.route('/')
def index():
    app.logger.debug('serving root URL /')
    if list_articles_Loup == [] :
        for fichier in list_path_Loup :
            list_articles_Loup.append(create_dict(fichier))
    if list_articles_Nino == [] :
        for fichier in list_path_Nino :
            list_articles_Nino.append(create_dict(fichier))
    if list_articles_Alex == [] :
        for fichier in list_path_Alex :
            list_articles_Alex.append(create_dict(fichier))
    if list_articles_SHN == [] :
        for fichier in list_path_SHN :
            list_articles_SHN.append(create_dict(fichier))
    return render_template('accueil.html')

@app.route('/Loup life')
def loup():
    app.logger.debug('Loup life')
    return render_template('Loup_cesure.html', articles = list_articles_Loup)

@app.route('/Nino life')
def nino():
    app.logger.debug('Nino life')
    return render_template('Nino_cesure.html', articles = list_articles_Nino)

@app.route('/Alexandre life')
def alexandre():
    app.logger.debug('Alexandre life')
    return render_template('Alexandre_echange.html', articles = list_articles_Alex)

@app.route('/SHN life')
def shn():
    app.logger.debug('SHN life')
    return render_template('SHN_CO.html', articles = list_articles_SHN)

@app.route('/new_post', methods = ["GET","POST"])
def new():
    app.logger.debug('New Post')
    app.logger.debug(path_articles)
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
                with open(str(path_articles+"/SHN/"+new_article["title"]+".txt"), "x") as fichier :
                    fichier.write(new_article["title"]+"\n")
                    fichier.write(new_article["news"])
                if new_article not in list_articles_SHN :
                    list_articles_SHN.append(new_article)
                return render_template("SHN_CO.html", articles = list_articles_SHN) 
            if username == "avilanoba" :
                with open(str(path_articles+"/Alex/"+new_article["title"]+".txt"), "x") as fichier :
                    fichier.write(new_article["title"]+"\n")
                    fichier.write(new_article["news"])
                if new_article not in list_articles_Alex :
                    list_articles_Alex.append(new_article)
                return render_template("Alexandre_echange.html", articles = list_articles_Alex) 
            if username == "mperrin" :
                with open(str(path_articles+"/SHN/"+new_article["title"]+".txt"), "x") as fichier :
                    fichier.write(new_article["title"]+"\n")
                    fichier.write(new_article["news"])
                if new_article not in list_articles_SHN :
                    list_articles_SHN.append(new_article)
                return render_template("SHN_CO.html", articles = list_articles_SHN) 
            if username == "lpetitjean" :
                with open(str(path_articles+"/Loup/"+new_article["title"]+".txt"), "x") as fichier :
                    fichier.write(new_article["title"]+"\n")
                    fichier.write(new_article["news"])
                if new_article not in list_articles_Loup :
                    list_articles_Loup.append(new_article)
                return render_template("Loup_cesure.html", articles = list_articles_Loup)
            if username == "nmolin" :
                with open(str(path_articles+"/Nino/"+new_article["title"]+".txt"), "x") as fichier :
                    fichier.write(new_article["title"]+"\n")
                    fichier.write(new_article["news"])
                if new_article not in list_articles_Nino :
                    list_articles_Nino.append(new_article)
                return render_template("Nino_cesure.html", articles = list_articles_Nino) 
    return render_template('new_post.html')

@app.route('/search/', methods=['GET'])
def search():
    app.logger.debug(request.args)
    searchword = request.args.get('pattern')
    pages = [list_articles_Nino, list_articles_Alex, list_articles_Loup, list_articles_SHN]
    for i in range(len(pages)) :
        for article in pages[i] :
            if searchword in article["title"] :
                if i == 0 :
                    return render_template('Nino_cesure.html', search = article)
                elif i == 1 :
                    return render_template('Alexandre_echange.html', search = article)
                elif i == 2 :
                    return render_template('Loup_cesure.html', search = article)
                elif i == 3 :
                    return render_template('SHN_CO.html', search = article)
    else : 
        abort(make_response('Your search "'+searchword+'" was not found.', 404))

# Script starts here
if __name__ == '__main__':
    from os import environ
    DEBUG = environ.get('DEBUG')
    app.run(port=8000, debug=DEBUG)

# VIM MODLINE
# vim: ai ts=4 sw=4 sts=4 expandtab fileencoding=utf8

"""
HELLO_STRINGS = {
        "cn": "????????????\n",
        "du": "Hallo wereld\n",
        "en": "Hello world\n",
        "fr": "Bonjour monde\n",
        "de": "Hallo Welt\n",
        "gr": "???????? ?????? ????????????\n",
        "it": "Ciao mondo\n",
        "jp": "?????????????????????\n",
        "kr": "???????????? ??????\n",
        "pt": "Ol?? mundo\n",
        "ru": "????????????????????, ??????\n",
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