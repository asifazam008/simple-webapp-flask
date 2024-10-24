from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return "Welcome to docker application...  "

@app.route('/is applicaton is running')
def hello():
    return "Yes.. its running now !!!"
if __name__ == '__main__':
    app.run(debug=True)
