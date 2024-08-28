from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index(name):
    return render_template('index.html')

@app.route('/whereami')
def whereami():
    return 'Ghana'
@app.route('/getName/<name>')
def get_name(name):
   return f'<h1>Hello there {name}!<h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')