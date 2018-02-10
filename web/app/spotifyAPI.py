import spotipy, json
import spotipy.util as util


def get_tracks(queries=["Post Malone"]):
    ids = []
    scope = 'playlist-modify-public'
    token = util.prompt_for_user_token(username="ASchneidman",scope=scope,client_id='7170451d1ae941d6967a9976a375cd00',client_secret='bc9a015ae6ce4f119d514b684998e084',redirect_uri='http://localhost/')
    sp = spotipy.Spotify(auth=token)
    for query in queries:
        print(query)
        results = sp.search(q='artist:{}'.format(query), limit=1, type='artist')
        items = results['artists']['items']
        if (len(items) != 0):
            res = items[0]['id']
            ids.append(res)
            print (res)

    tracks = []
    track_ids = []
    for id in ids:
        trackJSON = sp.artist_top_tracks(id)
        tracks_list = trackJSON['tracks']
        for i in tracks_list:
            tracks.append(i['name'])
            track_ids.append(i['id'])
        print(tracks[-1])
        print(track_ids[-1])
    return ids




if __name__ == '__main__':
    get_results()
