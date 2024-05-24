
from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    return "Main"

@app.route('/about')
def main():
    return "About"

@app.route('/store')
def main():
    return "Store"

if __name__ == "__main__":
    app.run()

