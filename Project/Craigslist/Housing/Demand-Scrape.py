from BeautifulSoup import BeautifulSoup
import requests
import numpy
import re

url = 'https://grandrapids.craigslist.org/search/hsw'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

listingtaglist = []
listingtags = soup.findAll("li", {"class" : "result-row"})
for listings in listingtags:
    listingtaglist.append(listings.text)
    print listings.text

pricetagslist = []
pricetags = soup.findAll("span", {"class" : ["result-price"]})
for prices in pricetags:
    pricetagslist.append(prices.text)
    print prices.text

masterarray = []
listingsarray = numpy.asarray(listingtaglist)
pricesarray = numpy.asarray(pricetagslist)

print(listingsarray.size)
print(pricesarray.size)

#masterarray = numpy.column_stack((listingsarray, pricesarray))

#numpy.savetxt("P:\TempFile.txt", masterarray, delimiter=" | ", fmt="%s")