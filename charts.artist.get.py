import json
from api_headers import *
pattern = r"[A-Za-z]"
def charts_artist_get():
	api_method = 'chart.artists.get'
	print("This option will provide you the list of the current top artists.")
	api_call = requests.get(base_url+api_method+'?page=1'+'&page_size=50'+'&format=json', params=headers, headers=data)
	api_call_json = api_call.json()
	artist_list = api_call_json['message']['body']['artist_list']
	return artist_list;
print(charts_artist_get())