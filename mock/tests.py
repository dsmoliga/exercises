import unittest
from unittest.mock import patch, Mock

from mock_exercise import get_elixir

"""class TestElixir(unittest.TestCase):
    def test_get_elixir(self):
        with patch('mock_exercise.requests.get') as mock_get:
            mock_get.json.return_value = {'name': 'a'}
            elixir = get_elixir(0)
            self.assertEquals(elixir, 'a')"""


class TestElixir(unittest.TestCase):

    @patch('mock_exercise.requests')
    def test_get_elixir(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'id': '568f24eb-55e6-4899-bd3b-8631118572b9', 'name': 'Hate Potion', 'effect': 'Revealed the worst traits of a person to the drinker',
                                           'sideEffects': None, 'characteristics': None, 'time': None, 'difficulty': 'Unknown', 'ingredients': [], 'inventors': [], 'manufacturer': None}

        mock_get.get.return_value = mock_response

        elixir = get_elixir(0)
        mock_get.get.assert_called_with(
            'https://wizard-world-api.herokuapp.com/Test/0')
        self.assertEqual(elixir, 'Hate Potion')


if __name__ == '__main__':
    unittest.main()
