from flask import Flask
from werkzeug.routing import BaseConverter

class FloatListConverter(BaseConverter):
    regex = r'\d+(?:,\d+)*,?'

    def to_python(self, value):
        return [float(x) for x in value.split(',')]

    def to_url(self, value):
        return ','.join(str(x) for x in value)

app = Flask(__name__)
app.url_map.converters['float_list'] = FloatListConverter

data = {'name': ['Ling', 'George', 'Ginger'],
        'height': [1.63, 1.87, 1.34]}


@app.route("/key/<name>/data/<int:index>")
def my_func(name, index):
#     return data[name][index]
      return str(data[name][index])


@app.route("/calculate/float_one/<float:num_one>/float_two/<float:num_two>")
def calc(num_one,num_two):
        res = num_one + num_two
        return str(res)



@app.route("/calc_list/<float_list:values>")
def calc_list(values):
        return str(sum(values))