from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, this is the Fitness Coach Bot!'

if __name__ == '__main__':
    app.run(debug=True)
