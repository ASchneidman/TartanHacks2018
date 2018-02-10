import spotipy, json
import spotipy.util as util


def get_tracks(queries=["Post Malone"]):
    ids = []
    scope = 'playlist-modify-public'
    username = "schneidmans"
    playlist_name = "Local"
    playlist_desc = "Local"
    token = util.prompt_for_user_token(username=username,scope=scope,client_id='314ebba86f7242bf816e56460f9514bb',client_secret='26cba47c6db841e5be7d7dfaeb3ef84',redirect_uri='http://localhost/')
    sp = spotipy.Spotify(auth=token)
    for query in queries:
        print(query)
        results = sp.search(q='artist:{}'.format(query), limit=1, type='artist')
        items = results['artists']['items']
        if (len(items) != 0):
            if (len(ids) > 10):
                break
            res = items[0]['id']
            ids.append(res)
            print (res)

    tracks = []
    track_ids = []
    num = 0
    for id in ids:
        artist_tracks = []
        trackJSON = sp.artist_top_tracks(id)
        tracks_list = trackJSON['tracks']
        for i in tracks_list:
            if (len(artist_tracks) > 4):
                break
            artist_tracks.append(i['id'])
            tracks.append(i['name'])
        for i in artist_tracks:
            track_ids.append(i)
    sp.trace = False
    playlist = sp.user_playlist_create(username, playlist_name)

    playlistid = playlist['id']
    results = sp.user_playlist_add_tracks(username, playlistid, track_ids)
    data = []
    data.append(playlistid)
    data.append(tracks)
    data.append(track_ids)
    return data




if __name__ == '__main__':
    get_results()
