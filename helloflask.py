import flask

app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World <a href="/number/1000000">click me1</a> <a href="/hello/Hod">click me2</a>'

@app.route('/hello/<name>')
def hello(name):
    return 'Hello there  <b>%s</b>. <a href="/">Homepage</a>' % name 

@app.route('/bye/<name>')
def bye(name):
    return "Goodbye <i>%s</i>" % name

@app.errorhandler(404)
def page_not_found(error):
    return "404: You're funny, there's no such page <a href='/'>Homepage</a>", 404 

app.run(debug=True)