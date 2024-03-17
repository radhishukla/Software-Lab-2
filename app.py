from flask import Flask, render_template

app = Flask(__name__)

@app.route("/name")
def name():
  return "Rads"


@app.route("/age)
           def age():
             return "20"

@app.route("/hello")
def hello():
  return "hello"
