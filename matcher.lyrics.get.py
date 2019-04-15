from api_headers import *
def matcher_lyrics_get():
	print("This api method prints the lyrics any track.\n")
	track_name = str(raw_input('Name the track:\n--->> '))
	artist_name = str(raw_input('Name the artist:\n--->>'))
	resp = requests.get(base_url+'matcher.lyrics.get?q_track={0}&q_artist={1}'.format(track_name, artist_name), params=headers, headers=data)
	resp_json = resp.json()
	if resp_json['message']['header']['status_code'] == 200:
		print("Lyrics found>>\n\n")
		lyrics = resp_json['message']['body']['lyrics']['lyrics_body']
		lyric_copyright = resp_json['message']['body']['lyrics']['lyrics_copyright']
		explicit_count = resp_json['message']['body']['lyrics']['explicit']
		lyric_id = resp_json['message']['body']['lyrics']['lyrics_id']
		updated_time = resp_json['message']['body']['lyrics']['updated_time']
		print(lyrics)
		print(lyric_copyright)
		print("The explicit count is {}".format(explicit_count))
		print("The lyric id is (you don't really need that): {}".format(lyric_id))
		print("The last updated time is {}:".format(updated_time))
	else:
		print("Error 404 Lyrics not found\nOr the server did not response")
		return 0;
matcher_lyrics_get()