from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello from my Flask App on Render!</h1>'

@app.route('/about')
def about():
    return '<h1>About Page</h1><p>This is a PaaS demo app.</p>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)