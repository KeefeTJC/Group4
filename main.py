TestMyProgram

import unittest class TestMyProgram(unittest.TestCase):
    
    def test_engineType(self):
        print("Texting")
if __name__ == '__main__':
    unittest.main()
    
   or
import unittest

class TestMyProgram(unittest.TestCase):
    
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        
    def test_isupper(self):
        self.assertTrue('FOO',isupper())
        self.assertFalse('Foo',isupper())
if __name__ == '__main__':
    unittest.main()
    
   or

import unittest
import myProgram as prog

class TestMyProgram(unittest.TestCase):
    def test_EngineType(self):
        vios = prog.Vehicle('4', 'petrol', 5, 180)
        self.assertEqual(vios.type_of_tank, 'petrol')

if __name__ == '__main__':
    unittest.main()      

Download Requests
#Use the Request library
import requests

# Set the target webpage
url = 'http://172.18.58.80/varsity'
webpage = requests.get(url)
# This will get the full webpage in text
print(webpage.text)
# Get and print the status code
print("Status code:")
print("\t *", webpage.status_code)
# Get the headers
h = requests.head(url)
print("Header:")
print("**********")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h,headers[x])
    print("**********")
    
# Modify the headers user-agent
headers = {'User-Agent': 'Mobile'}

# Test it on an external site
url2 = 'http://httpbin.org/headers'
request_header = requests.get(url2, headers=headers)
print(request_header.text)

Download scrapy
import scrapy
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://brickset.com/sets/year-2019']

    def parse(self, response):
        xpath_selector = '//img'
        for x in response.xpath(xpath_selector):
            newsel = '@src'
            yield {'Image Link': x.xpath(newsel).extract_first(), }

# To Recurse next page
        page_selector = '.next a ::attr(href)'
        next_page = response.css(page_selector).extract_first
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

#WK#NZS#KEEFE
