import urllib.request

response = urllib.request.urlopen('http://10.1.3.12/sec/?pt=7&cmd=get')
print(response.read())