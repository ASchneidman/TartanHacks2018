import spotipy, json
import spotipy.util as util


def get_results(queries=["Post Malone"]):

    scope = 'playlist-modify-public'
    username = 'ASchneidman'
    token = util.prompt_for_user_token(username=username,scope=scope,client_id='7170451d1ae941d6967a9976a375cd00',client_secret='bc9a015ae6ce4f119d514b684998e084',redirect_uri='http://localhost/')
    sp = spotipy.Spotify(auth=token)
    for query in queries:
        print(query)
        results = sp.search(q='artist:{}'.format(query), limit=1, type='artist')
        items = results['artists']['items'][0]['id']
        print (items)

if __name__ == '__main__':
    get_results()
