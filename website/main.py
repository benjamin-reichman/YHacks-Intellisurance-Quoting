from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

app = Flask(__name__)  # create the application instance :)
app.config.from_object(__name__)  # load config from this file , flaskr.py

@app.route(r'/')
def landingpage_with_survey():
    return render_template('index2.html')

@app.route(r'/processing', methods=["POST"])
def gettingdata():
    request.form["gender"]
    print(request.form.get)
    return "yay"


if __name__ == '__main__':
    app.run()
