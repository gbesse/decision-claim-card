import hashlib
import unittest

from claim_card import card


class ClaimCardTests(unittest.TestCase):
    def test_card_has_provenance_and_caveat(self):
        text = card({"key": "sample", "hard": {"n_items": 10, "accuracy": 0.7, "coverage": 1}}, "https://example.org/data.json", "abc", "fr")
        self.assertIn("70.0%", text)
        self.assertIn("https://example.org/data.json", text)
        self.assertIn("ne relance pas", text)

    def test_rejects_missing_accuracy(self):
        with self.assertRaises(ValueError):
            card({"hard": {"n_items": 10}}, "https://example.org/data", "abc")

    def test_works_with_published_jevbench_shape(self):
        data = {"key": "jeff", "display": "jeff", "licence": "MIT", "hard": {"n_items": 220, "accuracy": 0.377272727, "coverage": 1}}
        text = card(data, "https://github.com/fstandhartinger/jevbench/blob/main/results/v1.2/additions/jeff.json", "abc")
        self.assertIn("37.7%", text)
        self.assertIn("220", text)
