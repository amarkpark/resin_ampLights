import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return os.getenv('LTBL', "Future's so bright, gotta wear shades!")

@app.route('/exon')
def on():
	return "External lights are now ON"

@app.route('/exoff')
def off():
	return "External lights are now OFF"

@app.route('/inon')
def on():
	return "Internal lights are now ON"

@app.route('/inoff')
def off():
	return "Internal lights are now OFF"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)