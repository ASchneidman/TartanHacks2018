import spotipy
import spotipy.util as util
sp = spotipy.Spotify()

def get_results(queries=["Post Malone"]):
    for query in queries:
        print(query)
        results = sp.search(q='artist:{}'.format(query), limit=1)
        print (results)

if __name__ == '__main__':
    get_results()
