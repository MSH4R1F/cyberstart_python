import urllib.request
import urllib

request = urllib.request.Request("http://127.0.0.1:8082")
response = urllib.request.urlopen(request)
html = response.read()
print(html)

data = urllib.parse.urlencode({'user' : 'tweetbotuser', 'status-update'  : 'alientest'})
data = data.encode("utf-8")
request = urllib.request.Request("http://127.0.0.1:8082", headers={'x-api-key':'tweetbotkeyv1'}, data=data)
response = urllib.request.urlopen(request)
print(response.read())
