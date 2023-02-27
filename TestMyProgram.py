import unittest
import requests


url = "http://172.18.58.80/index.html"


# Each test class must be a subclass of unittest.TestCase
# The class should be named as TestXXXX to indicate to the program that it is a test program
class TestMyProgram(unittest.TestCase):

    # All methods should be named as test_XXXX to indicate that it is a test case

    # Checking whether the url is responding to requests
    def test_TestUrl(self):
        try:
            resp = requests.get(url)
            if int(resp.status_code) == 200:
                print("[TestUrl] URL OK")
            else:
                print("[TestUrl] Requested URL not found")
        except Exception as e:
            print("[TestUrl] Error: ", {e})

    def test_TestCase_2(self):
        print("[TestCase_2] Test case 2")

import unittest
from scrapytest import NewSpider

class TestNewSpider(unittest.TestCase):
    def test_start_urls(self):
        self.assertEqual(NewSpider().start_urls[0], 'http://172.18.58.80/varsity')

# Must invoke the unittest.main() methods
if __name__ == '_main_':
    unittest.main()
