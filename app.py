from flask import flask
app=flask(__name__)

@app.route("/")
def home():
    return "hello devops world v1"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000)