from flask import Flask, render_template, jsonify, request
import json
import requests
import pickle
import pandas as pd
app = Flask(__name__)

APIkey = {'apikey' : 'ha299393881404988495032524468396'} 
ids = pickle.load(open('pickles/ids_df.pkl', 'rb'))

with open("countries.geo.json") as f:
	alljson = json.load(f)

#with open("idCountry.csv") as f:
#	alljson = json.load(f)

@app.route("/")
def main():
    return render_template('index.html')


@app.route("/alljson")
def load_all():
	return jsonify(alljson)

@app.route("/dataframes/bars")
def load_bars():
	bars = pickle.load(open('pickles/bars_df.pkl', 'rb'))
	return bars.to_csv()

@app.route("/dataframes/unesco")
def load_unesco():
	unesco = pickle.load(open('pickles/unesco_df.pkl', 'rb'))
	return unesco.to_csv()

@app.route("/dataframes/heritage")
def load_heritage():
	heritage = pickle.load(open('pickles/heritage_df.pkl', 'rb'))
	return heritage.to_csv()

@app.route("/dataframes/museums")
def load_museums():
	museums = pickle.load(open('pickles/museums_df.pkl', 'rb'))
	return museums.to_csv()

@app.route("/dataframes/parks_percent")
def load_parks_percent():
	parks_percent = pickle.load(open('pickles/parks_percent_df.pkl', 'rb'))
	return parks_percent.to_csv()	

@app.route("/dataframes/restau_per_ca")
def load_restau_per_ca():
	restau_per_ca = pickle.load(open('pickles/restau_per_ca_df.pkl', 'rb'))
	return restau_per_ca.to_csv()

@app.route("/dataframes/tourist_per_cent")
def load_tourist_per_cent():
	tourist_per_cent = pickle.load(open('pickles/tourist_per_cent_df.pkl', 'rb'))
	return tourist_per_cent.to_csv()

@app.route("/dataframes/bars_percent")
def load_bars_percent():
	bars_percent = pickle.load(open('pickles/bars_percent_df.pkl', 'rb'))
	return bars_percent.to_csv()

@app.route("/dataframes/nightclubs")
def load_nightclubs():
	nightclubs = pickle.load(open('pickles/nightclubs_df.pkl', 'rb'))
	return nightclubs.to_csv()

@app.route("/dataframes/arcades")
def load_arcades():
	arcades = pickle.load(open('pickles/arcades_df.pkl', 'rb'))
	return arcades.to_csv()

@app.route("/dataframes/temps")
def load_temps():
	name2id = dict(ids.set_index('name'))
	temps = pd.read_csv('temp_countries.csv', sep=';')
	temps['temp'] =  temps['temp'].apply(lambda x: x.split('\t')[-1] )
	temps['temp'] =  temps['temp'].apply(float)
	temps['id'] = temps['country'].apply(lambda x: name2id['id'][x] if x in name2id['id'] else None)
	temps = temps.dropna().drop('country', axis=1).set_index('id')
	return temps.to_csv()

# @app.route("/airport/<country>")
# def get_airport(country=None):
# 	if(country == 'United States of America'):
# 		country = 'United States'
# 	print(country)
# 	country_req = "http://partners.api.skyscanner.net/apiservices/autosuggest/v1.0/FR/eur/en-US?query={}&apikey=ha299393881404988495032524468396".format(country)
# 	r1 = requests.get(country_req, params=APIkey)
# 	if r1.status_code != 200:
# 		print("error!")
# 		return None
# 	j1 = r1.json()
# 	all_airports = [city['PlaceId'] for city in j1['Places']]
	
# 	data_dict = []
# 	for (n,p) in zip(all_names, prices):
# 		item = {
# 			'name' : n,
# 			'price' : p
# 		}
# 		data_dict.append(item)

# 	return jsonify(data_dict)




@app.route("/cost/<country>")
def get_search(country=None):
	if(country == 'United States of America'):
		country = 'United States'
	print(country)
	country_req = "http://partners.api.skyscanner.net/apiservices/autosuggest/v1.0/FR/eur/en-US?query={}&apikey=ha299393881404988495032524468396".format(country)
	r1 = requests.get(country_req, params=APIkey)
	if r1.status_code != 200:
		print("error!")
		return None
	j1 = r1.json()
	all_airports = [city['PlaceId'] for city in j1['Places']]
	all_names = [city['PlaceName'] for city in j1['Places']]

	# remove first elem that is a search for whole country
	all_airports = all_airports[1:]
	all_names = all_names[1:]

	prices = []
	for airport in all_airports:
		country = 'FR'
		currency = 'eur'
		locale = 'en-US'
		originPlace = 'gva'
		destinationPlace = airport
		outboundPartialDate = '2017-12'
		inboundPartialDate = '2017-12'

		url_request = "http://partners.api.skyscanner.net/apiservices/browsedates/v1.0/{co}/{cu}/{l}/{orig}/{dest}/{outD}/{inD}".format(
						co = country, cu = currency, l=locale, orig=originPlace, 
				dest=destinationPlace, outD=outboundPartialDate, inD=inboundPartialDate)
	    
		r = requests.get(url_request, params=APIkey)
		if r.status_code != 200:
			print("error !")
			return None
		j = r.json()
		if len(j['Dates']['InboundDates']) > 0:
			prices.append(j['Dates']['InboundDates'][0]['Price'])
		else:
			prices.append(None)

	data_dict = []
	for (n,p, a) in zip(all_names, prices, all_airports):
		item = {
			'name' : n,
			'price' : p,
			'airport': a
		}
		data_dict.append(item)

	return jsonify(data_dict)


if __name__ == "__main__":
	app.run()