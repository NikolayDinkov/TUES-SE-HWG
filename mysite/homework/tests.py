from django.test import TestCase
import requests
from homework.weatherApiFunc import WeatherApiFunc
from unittest.mock import Mock, patch

class TestMyApiFunc(TestCase):
    def setUp(self):
        self.weatherFunc = WeatherApiFunc()
        self.weather = {
            "city": "Sofia",
            "data": [
                {
                    "date":  "Mon, 10 Jan 2022 08:45:57 GMT",
                    "temperature": 4,
                },
                {
                    "date":  "Tue, 11 Jan 2022 08:45:57 GMT",
                    "temperature": 5,
                },
                {
                    "date":  "Wed, 12 Jan 2022 08:45:57 GMT",
                    "temperature": 3,
                },
                {
                    "date":  "Thu, 13 Jan 2022 08:45:57 GMT",
                    "temperature": 8,
                },
                {
                    "date":  "Fri, 14 Jan 2022 08:45:57 GMT",
                    "temperature": 5,
                }]
            }

    def tearDown(self):
        pass

    @patch("requests.post")
    def testMaxTemp(self, mockedRequests):
        mockedRequests.return_value.json = Mock(return_value = self.weather)
        response = self.weatherFunc.maxTemp()
        self.assertEqual(response, 8)
        
    @patch("requests.post")
    def testAvgTemp(self, mockedRequests):
        mockedRequests.return_value.json = Mock(return_value = self.weather)
        response = self.weatherFunc.avgTemp()
        self.assertEqual(response, 5.0)

    @patch("requests.post")
    def testMinTemp(self, mockedRequests):
        mockedRequests.return_value.json = Mock(return_value = self.weather)
        response = self.weatherFunc.minTemp()
        self.assertEqual(response, 3)

