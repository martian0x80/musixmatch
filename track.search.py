from api_headers import *
query_url = base_url+'track.search?'
start = '''
This api method searches for tracks and it is highly advanced search.
Commands:
\'tname\' :: To search for a track name.
\'aname\' :: To search for track by artists' name/
\'taname\':: To search between keywords from artists' name and track name.
\'qlyric\':: To search between lyrics.
\'q\'     :: To search between lyrics, artists' name and track name.
\'ps\'    :: To set the page size to a different value.[default=10]
'''
print(start)
page_size = str(10)
def request(string1, string2):
	resp = requests.get(query_url+string1+'='+string2+'&page_size='+page_size+'&page=1&s_track_rating=asc&format=json', params=headers, headers=data)
	resp_json = resp.json()
	return resp_json['message']['body']['track_list'];
def interating_json_array(array):
	data = ['updated_time','album_name','artist_name','track_name','track_id']
	try:
		for i in range(0,int(page_size)):
			print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
			for j in range(0,len(data)):
				print(data[j-1] + ' = ' + str(array[i]['track'][data[j-1]]))
	except IndexError:
		print("The query was too long, sorry :( ")
def go_back(string):
	if string == '99':
		print('Going back...')
		track_search()
def ask_page_size():
	print("Enter the value below")
	print("Notice: A value between 1-100 is accepted.")
	pattern = r"[0-9]"
	pattern1 = r"[0-9][0-9]"
	try:
		globals()['page_size'] = str(input("<< "))
		if re.search(pattern, page_size):
			print("The page size is set to {}".format(page_size))
			track_search()
		elif re.search(pattern1, page_size):
			print("The Page size is set to {}".format(page_size))
			track_search()
		else:
			print("A value between 1-100 is accepted")
	except ValueError:
		print("Only enter a number")
		ask_page_size()
def track_name():
	input_parameter = 'q_track'
	print("You choosed the option to search track\n")
	print("To go back type \'99\'")
	print("Or enter the name of track you wanna search")
	track = str(input(">> "))
	go_back(track)
	array = request(input_parameter, track)
	interating_json_array(array)
def artist_name():
	input_parameter = 'q_artist'
	print("You choosed the option to search with artists' name\n")
	print("To go back type \'99\'")
	print("Or enter the artist's name")
	artist = str(input(">> "))
	go_back(artist)
	array = request(input_parameter, artist)
	interating_json_array(array)
def track_artist_name():
	input_parameter = 'q_track_artist'
	print("You have choosed the option to search with track name + artist name\n")
	print("To go back type \'99\'")
	print("Or enter the keywords")
	track_artist = str(input(">> "))
	go_back(track_artist)
	array = request(input_parameter, track_artist)
	interating_json_array(array)
def lyric_search():
	input_parameter = 'q_lyrics'
	print("You have choosed the option to search with lyrics\n")
	print("To go back type \'99\'")
	print("Or enter the keywords")
	lyric = str(input(">> "))
	go_back(lyric)
	array = request(input_parameter, lyric)
	interating_json_array(array)
def universal_search():
	input_parameter = 'q'
	print("You have choosed the option to search between lyrics, track title and artists' name.\n")
	print("To go back type \'99\'")
	print("Or enter the keywords")
	q = str(input(">> "))
	go_back(q)
	array = request(input_parameter, q)
	interating_json_array(array)
def invalid_option():
	print("You entered an invalid options\n Continuing...")
	track_search()
def track_search():
	take_options = str(input("\n>> "))
	if take_options == 'ps':
		ask_page_size()
	elif take_options == 'tname':
		track_name()
	elif take_options == 'aname':
		artist_name()
	elif take_options == 'taname':
		track_artist_name()
	elif take_options == 'qlyric':
		lyric_search()
	elif take_options == 'q':
		universal_search()
	elif take_options == 'help':
		print(start)
		track_search()
	elif take_options == '':
		track_search()
	elif take_options == 'exit':
		pass
	else:
		invalid_option()
track_search()
#Powered by MusixMatch API
