import os
from flask import Flask, render_template, request
from dbActions import json_query
import requests
import json

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def index_page():
    return render_template('assignment11.html')

@app.route("/assignment11/users")
def assignment11_site():
    query = "select * from users"
    query_result = json_query(query=query)
    return json.dumps(query_result)

@app.route("/assignment11/outer_source")
def assignment11_outer_source():
    if len(request.args) > 0: # called from form submit (b.e)
        user_id = request.args['user_id']
        if user_id:
            user = requests.get(url=f"https://reqres.in/api/users/{user_id}")
            user_data = user.json()['data']
            return render_template("outer_form.html", user = user_data)
        else:
            return render_template("outer_form.html")
    else:
        return render_template("outer_form.html")


if __name__ == '__main__':
    #   Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.secret_key = '123'
    app.run(host='127.0.0.1', port=port)

