import unittest

import sujmarkov


class TestGetNGrams(unittest.TestCase):

    def test_get_ngrams_from_string(self):
        """Test that we fetch ngrams from a string.
        """
        original_string = "raspberry"

        bigrams = list(sujmarkov.get_ngrams(original_string, n=2))
        self.assertEqual(
            bigrams,
            ["ra", "as", "sp", "pb", "be", "er", "rr", "ry"]
        )

        trigrams = list(sujmarkov.get_ngrams(original_string, n=3))
        self.assertEqual(
            trigrams,
            ["ras", "asp", "spb", "pbe", "ber", "err", "rry"]
        )

        fourgrams = list(sujmarkov.get_ngrams(original_string, n=4))
        self.assertEqual(
            fourgrams,
            ["rasp", "aspb", "spbe", "pber", "berr", "erry"]
        )

    def test_ngrams_from_empty(self):
        """Empty input will return None
        """
        no_ngrams = sujmarkov.get_ngrams([])
        for x in no_ngrams:
            self.fail("We should not have any ngrams")

    def test_ngrams_from_list(self):
        """We should be able to handle lists as well.
        """
        sequence = ["one", "two", "three", "four", "five"]

        bigrams = list(sujmarkov.get_ngrams(sequence, n=2))
        self.assertEqual(
            bigrams,
            [["one", "two"], ["two", "three"], ["three", "four"], ["four", "five"]]
        )
