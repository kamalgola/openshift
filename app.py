import os
from flask import Flask
app = Flask(__name__)
@app.route("/")
def main():
  return "Welcome!!!"

@app.route('How are you?')
def hello():
  return "I am doing fine."

if __name__ "" "__main__"
  app.run(host="0.0.0.0", port=8080)
