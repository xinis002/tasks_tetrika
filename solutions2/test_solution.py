import unittest
from unittest.mock import patch, Mock
from collections import defaultdict

from bs4 import BeautifulSoup

from solutions2.solution import save_to_csv, get_page, parse_all_pages

import os
import csv

class TestCounter(unittest.TestCase):
    def setUp(self):
        self.sample_counts= defaultdict(int, {
            'А': 10,
            'Б': 5,
            'В': 3,
        })
        self.test_file = "test_beasts.csv"

    def test_save_csv_creates_file(self):
        save_to_csv(self.sample_counts)
        self.assertTrue(os.path.exists("beasts.csv"))


    def test_save_csv_content(self):
        save_to_csv(self.sample_counts)
        with open("beasts.csv", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = list(reader)

        expected_rows = [['А', '10'], ['Б', '5'], ['В', '3']]
        self.assertEqual(rows[:3], expected_rows)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    @patch("solutions2.solution.requests.get")
    def test_get_page(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "<html><body><p>Hello</p></body></html>"
        mock_get.return_value = mock_response

        soup = get_page("/fake-url")
        self.assertEqual(soup.find("p").text, "Hello")

    @patch("solutions2.solution.get_page")
    def test_parse_all_pages_with_mocked_html(self, mock_get_page):
        html = '''
            <div class="mw-category-group">
                <ul>
                    <li>Архар</li>
                    <li>Ёжик</li>
                    <li>Bear</li>
                    <li></li>
                </ul>
            </div>
            <a>Следующая страница</a>
            '''

        soup_mock = BeautifulSoup(html, "lxml")
        mock_get_page.side_effect = [soup_mock, soup_mock]

        with patch("solutions2.solution.time.sleep"):
            result = parse_all_pages()

        self.assertEqual(result["А"], 1)
        self.assertEqual(result["Е"], 1)  # Ё → Е
        self.assertNotIn("B", result)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


if __name__ == '__main__':
    unittest.main()