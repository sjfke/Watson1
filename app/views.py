# views.py

from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

from app import app

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/admin')
def hello_admin():
   return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
   if name == 'admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest', guest=name))


@app.route('/success/<name>')
def success(name):
   return render_template('success.html', name=name)


@app.route('/login', methods=['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success', name=user))
   else:
      # user = request.args.get('nm', '')
      return render_template('login.html')

  
@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello.html', name=user)


@app.route('/result')
def result():
   dict = {'phy':50, 'che':60, 'maths':70}
   return render_template('result.html', result=dict)


@app.route('/say_hello')
def say_hello():
   return render_template('say_hello.html')


@app.route('/watson_nlc')
def watson_nlc():
    
    import json
    from watson_developer_cloud import NaturalLanguageUnderstandingV1
    from watson_developer_cloud.natural_language_understanding_v1 import Features, CategoriesOptions

    from ConfigParser import SafeConfigParser
    config = SafeConfigParser()
    config.read('/etc/watson_cfg.ini')

    natural_language_understanding = NaturalLanguageUnderstandingV1(
        username=config.get('watson', 'username'),
        password=config.get('watson', 'password'),
        version=config.get('watson', 'version')
    )


    response = natural_language_understanding.analyze(
        url='https://fr.wikipedia.org/wiki/Gen%C3%A8ve',
        features=Features(
            categories=CategoriesOptions()
        )
    )

    return(json.dumps(response))
