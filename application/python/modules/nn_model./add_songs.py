songs_from_vk = '''

 '''

songs = [song for song in songs_from_vk.split('\n') if len(song) > 0 and ':' not in song]

with open('songs.txt', 'a') as file:
  for song in songs:
    file.write(f'{song}\n')
