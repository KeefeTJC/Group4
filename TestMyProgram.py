import unittest
    from scrapytest import NewSpider

    class TestNewSpider(unittest.TestCase):
        def test_start_urls(self):
            self.assertEqual(NewSpider().start_urls[0], 'http://172.18.58.80/varsity')


    def test_TestCase_2(self):
        print("[TestCase_2] Test case 2")

# Must invoke the unittest.main() methods
if _name_ == '_main_':
    unittest.main()
