from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd

# Nasa Mars News

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://mars.nasa.gov/news/'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')
time.sleep(30)


news = soup.find('li', class_='slide')
#print(news)
#print(news.prettify())

title = soup.find('div', class_='bottom_gradient')

while title is None:
    time.sleep(1)

news_title_text = (title.text)

paragraph = soup.find('div', class_='article_teaser_body')
news_paragraph_text = (paragraph.text)

print(f"The title of the article is: {news_title_text}")
print("")
print(f"The paragraph text of the article is: {news_paragraph_text}")


# JPL Mars Space Images - Featured Image

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')
time.sleep(1)

img_2 = soup.find('a', class_="button fancybox")
print(img_2)


href = soup.find('a', class_="button fancybox")['data-fancybox-href']
print(href)

featured_image_url = "https://www.jpl.nasa.gov" + href

print(featured_image_url)

## Mars Weather
url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')
time.sleep(10)

twitter7 = soup.find('div', lang="en")
print(twitter7.text)

mars_weather = (twitter7.text)
print(mars_weather)

# Mars Facts

url = 'https://space-facts.com/mars/'

tables = pd.read_html(url)
tables[0]

mars_facts = tables[0]

mars_facts_html_table = mars_facts.to_html('mars_facts_table.html', header=False, bold_rows=True, index=False)
mars_facts_html_table


# Mars Hemispheres

hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg"},
]

