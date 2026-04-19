import urllib.request, json
url = 'https://unsplash.com/napi/search/photos?query=competitive+swimming&per_page=15&page=1'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())
    for idx, photo in enumerate(data['results']):
        print(str(idx) + ': ' + photo['urls']['regular'] + ' - ' + str(photo['alt_description']))
