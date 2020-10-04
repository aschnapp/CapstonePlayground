from flask import Flask

server = Flask(__name__)

print("heerrre")

@server.route('/')
def index():
    return 'Hello, World!'
