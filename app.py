import os
from flask import Flask, render_template
from data import Data

app = Flask(__name__)


def __init__(self):
	"""."""
	self._client = Client()


@app.route('/')
def hello():
    return "para acessar as coisas da API veja documentacao!"



@app.route('/confirmed/<country>')
def confirmed(country):
	d = Data()
	figdata_png = d.confirmed(country=country)
	json = d.convert_json(img_base=figdata_png)
	return app.response_class(
        response=json,
        status=200,
        mimetype='application/json'
    )


@app.route('/deaths/<country>')
def deaths(country):
	d = Data()
	figdata_png = d.deaths(country=country)
	json = d.convert_json(img_base=figdata_png)
	return app.response_class(
        response=json,
        status=200,
        mimetype='application/json'
    )


@app.route('/recovered/<country>')
def recovered(country):
	d = Data()
	figdata_png = d.recovered(country=country)
	json = d.convert_json(img_base=figdata_png)
	return app.response_class(
        response=json,
        status=200,
        mimetype='application/json'
    )


@app.route('/countries_confirmed')
def countries_confirmed():
	d = Data()
	figdata_png = d.countries_confirmed()
	json = d.convert_json(img_base=figdata_png)
	return app.response_class(
        response=json,
        status=200,
        mimetype='application/json'
    )


@app.route('/countries_recovered')
def countries_recovered():
	d = Data()
	figdata_png = d.countries_recovered()
	json = d.convert_json(img_base=figdata_png)
	return app.response_class(
        response=json,
        status=200,
        mimetype='application/json'
    )



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
