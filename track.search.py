from api_headers import *
query_url = base_url+'track.search?'
start = '''
This api method searches for tracks and it is highly advanced search.
You know the name of track, then type, \'tname\'
If not, you know the artist then type, \'aname\'
Don't worry if you have a sluggish memory and know some keywords either from the artist name or track name, type \'taname\'

Fine, if you don't anything from its name, then you might be knowing some keywords from lyrics I can search that for you just type \'qlyric\'
\n\n\n
OKKK, If you are a mental memory patient or suffering from some kind of memory loss you still can search anything from the these categories i.e., artist, track, lyrics.\n
You can type \'q\' for this kind of universal search.
You can set the page_size value to anything by typing ps and then when prompt typing its value(ranging from 1 to 100) default is set 10.
Now we are ready to go
'''
print(start)
page_size = str(10)
def request(string1, string2):
	resp = requests.get(query_url+string1+'='+string2+'&page_size='+page_size+'&page=1&s_track_rating=asc&format=json', params=headers, headers=data)
	resp_json = resp.json()
	return resp_json['message']['body']['track_list'];
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
	print("You choosed the option search track\n")
	print("To go back type \'99\'")
	print("Or enter the name of track you wanna search")
	track = str(input(">> "))
	if track == '99':
		print("Going back...")
		track_search()
	else:
		array = request(input_parameter, track)
		data = ['artist_id','updated_time','album_name','album_id','artist_name','track_name','track_id']
		for i in range(0,len(array)):
			print(array[0]['track'][data[i]])
def invalid_option():
	print("You entered an invalid options\n Continuing...")
	track_search()
def track_search():
	take_options = str(input("\n>> "))
	if take_options == 'ps':
		ask_page_size()
	elif take_options == 'tname':
		track_name()
	elif take_options == 'help':
		print(start)
		track_search()
	elif take_options == 'exit':
		pass
	elif take_options == '':
		invalid_option()
	else:
		invalid_option()
track_search()