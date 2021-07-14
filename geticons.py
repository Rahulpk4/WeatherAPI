import urllib.request
import os

days = ['01d.png', '02d.png', '03d.png', '04d.png', '09d.png', '10d.png', '11d.png', '13n.png', '50d.png']
nights = ['01n.png', '02n.png', '03n.png', '04n.png', '09n.png', '10n.png', '11n.png', '13n.png', '50n.png']

base_url = 'https://openweathermap.org/img/w/'

img_dir = "./Images/"

if not os.path.exists(img_dir):
    os.mkdir(img_dir)


for day in days:
    filename = img_dir+day
    urllib.request.urlretrieve(base_url+day, filename)

for night in nights:
    filename = img_dir+night
    urllib.request.urlretrieve(base_url+night, filename)