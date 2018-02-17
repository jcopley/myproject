from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "<H1>Hello world! What's Up?</H1>"

if __name__ == "__main__":
	app.run(host='0.0.0.0')
