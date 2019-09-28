from unittest import TestCase, main
from endpoint import app, redis, queue
from rq.job import Job
from rq.exceptions import NoSuchJobError
from shutil import make_archive
from requests import get
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
from redis import Redis


class TestEndpoint(TestCase):
    def setUp(self):
        self.app = app
        self.redis = redis = Redis()
        self.queue = queue
        self.client = self.app.test_client()
        with open('sample_html', 'r') as f:
            self.sample_html = f.read()
        self.soup = BeautifulSoup(self.sample_html, 'html.parser')\
                        .html.body

    def test_no_such_job(self):
        with self.assertRaises(NoSuchJobError) as e:
            Job.fetch('test', connection = self.redis)

    def test_no_such_folder(self):
        with self.assertRaises(FileNotFoundError) as e:
            make_archive('test', 'zip', f"data/test.com")

    def test_connection_error(self):
        with self.assertRaises(ConnectionError) as e:
            get('http://dwadwadwadaw.dwadwa')

    def test_download_text(self):
        self.assertRegex(self.soup.text, "Stack Overflow")

    def test_download_images(self):
        self.assertAlmostEqual(len(self.soup.find_all('img')), 30)


if __name__ == '__main__':
    main()
