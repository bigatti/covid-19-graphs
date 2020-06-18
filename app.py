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
	return render_template('view.html', result=figdata_png)


@app.route('/deaths/<country>')
def deaths(country):
	d = Data()
	figdata_png = d.deaths(country=country)
	return render_template('view.html', result=figdata_png)


@app.route('/recovered/<country>')
def recovered(country):
	d = Data()
	figdata_png = d.recovered(country=country)
	return render_template('view.html', result=figdata_png)


@app.route('/countries_confirmed')
def countries_confirmed():
	d = Data()
	figdata_png = d.countries_confirmed()
	return render_template('view.html', result=figdata_png)


@app.route('/countries_recovered')
def countries_recovered():
	d = Data()
	figdata_png = d.countries_recovered()
	return render_template('view.html', result=figdata_png)



if __name__ == '__main__':
    app.run()
