import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return os.getenv('LTBL', "Future's so bright, gotta wear shades!")

@app.route('/exon')
def exon():
	return "External lights are now ON"

@app.route('/exoff')
def exoff():
	return "External lights are now OFF"

@app.route('/inon')
def inon():
	return "Internal lights are now ON"

@app.route('/inoff')
def inoff():
	return "Internal lights are now OFF"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)