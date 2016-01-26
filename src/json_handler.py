import json, urllib2

def get_matches_data():
	return json.load(urllib2.urlopen("http://csgolounge.com/api/matches_stats"))

def get_matches():
	return json.load(urllib2.urlopen("http://csgolounge.com/api/matches"))