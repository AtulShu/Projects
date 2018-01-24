import re
import urllib.request

city = input('enter your city:')
url = "https://www.weather-forecast.com/locations/"+ city +"/forecasts/latest"
data = urllib.request.urlopen(url).read()
data1 = data.decode('utf-8')

m = re.search('span class="phrase">', data1)

start = m.end()

end = start + 106

newS = data1[start:end]
print(newS)

m = re.search("</span>", newS)

final = newS[start:end]
print(final)
input('')
