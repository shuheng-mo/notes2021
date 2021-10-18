from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def my_func():
    return "<b>Hello</b> World!"

@app.route("/calculate/<number_one>/<number_two>")
def cal_floats(number_one, number_two):
    # result = request.view_args['number_one'] + request.view_args['number_two']
    result = float(number_one) + float(number_two)
    return "<b>"+ str(result)+"</b>"
