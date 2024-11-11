import unittest
from scraper import get_itc_response, get_news


class ItcScraper(unittest.TestCase):
    def test_access_by_url(self):
        response = get_itc_response()
        self.assertEqual(response.status_code, 200)

    def test_find_news(self):
        news = get_news()
        self.assertEqual(type(news), list)
        self.assertTrue(len(news) > 1)

    def test_has_attributes(self):
        post = get_news()[0]

        self.assertEqual(type(post), dict)
        self.assertTrue(post['title'])
        self.assertTrue(post['href'])
        self.assertTrue(post['category'])
        self.assertTrue(post['publish_date'])



if __name__ == '__main__':
    unittest.main()


