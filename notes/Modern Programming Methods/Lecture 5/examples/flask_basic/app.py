from flask import Flask, request

app = Flask(__name__)

clients = ["TomCruise", "HalleBerry"]


@app.route("/therightplacetogo")
def my_func():
    client_name = request.args.get('name', default=None)
    if client_name in clients:
        return f"<b>Hello</b> {client_name}"
    else:
        return f"Are you in the right place"
