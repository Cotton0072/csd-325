# test_cities.py
import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for the city_country function with language."""

    def test_city_country_population_language_paris(self):
        result = city_country("Paris", "France", 2148000, "French")
        self.assertEqual(result, "Paris, France - population 2148000, French")

    def test_city_country_population_newyork(self):
        result = city_country("New York", "United States", 8419600, "English")
        self.assertEqual(result, "New York, United States - population 8419600, English")

    def test_city_country_population_tokyo(self):
        result = city_country("Tokyo", "Japan", 13960000, "Japanese")
        self.assertEqual(result, "Tokyo, Japan - population 13960000, Japanese")

if __name__ == '__main__':
    unittest.main()
