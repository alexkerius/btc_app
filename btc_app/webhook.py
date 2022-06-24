import flask

app=flask.Flask(__name__)

@app.route("/",methods=["POST"])

def webhook():
    if flask.request.method=="POST":
        print(flask.request.json)
        return "200 OK"
    else:
        flask.abort(400)

if __name__ == "__main__":
    app.run(debug=False)