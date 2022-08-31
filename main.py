import urllib
import urllib.request
url = 'https://github.com/BrunoGuimar'
try:
    site = urllib.request.urlopen(url)
except urllib.error.URLError:
    print('WEBSITE NOT ACESSIBLE')
else:
    print('WEBSITE ON AIR !')