from cProfile import label
import requests
from bs4 import BeautifulSoup
from inflection import titleize





r = requests.get('https://theskylive.com/moon-info#:~:text=The%20Moon%20is%20currently%20in,is%20%2D4.99%20(JPL)')
soup = BeautifulSoup(r.text, 'html.parser')
labels = soup.find_all(label)
# ar = soup.find_all(ar)

for label in labels:
    print(label['keyinfobox'])