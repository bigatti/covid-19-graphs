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
	return figdata_png


@app.route('/deaths/<country>')
def deaths(country):
	d = Data()
	figdata_png = d.deaths(country=country)
	return figdata_png


@app.route('/recovered/<country>')
def recovered(country):
	d = Data()
	figdata_png = d.recovered(country=country)
	return figdata_png


@app.route('/countries_confirmed')
def countries_confirmed():
	d = Data()
	figdata_png = d.countries_confirmed()
	return figdata_png


@app.route('/countries_recovered')
def countries_recovered():
	d = Data()
	figdata_png = d.countries_recovered()
	return figdata_png



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
