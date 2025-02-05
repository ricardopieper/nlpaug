import unittest

import nlpaug.augmenter.word as naw
from nlpaug.util import Action


class TestRandom(unittest.TestCase):
    def test_empty_input_for_swap(self):
        texts = ['']
        aug = naw.RandomWordAug(action=Action.SWAP)
        for text in texts:
            augmented_text = aug.augment(text)

            self.assertEqual(text, augmented_text)

        self.assertEqual(1, len(texts))
        self.assertEqual(0, len(texts[0]))

        tokens = [None]
        aug = naw.RandomWordAug(action=Action.SWAP)
        for t in tokens:
            augmented_text = aug.augment(t)
            self.assertEqual(augmented_text, None)

        self.assertEqual(len(tokens), 1)

    def test_empty_input_for_delete(self):
        texts = ['']
        aug = naw.RandomWordAug(action=Action.DELETE)
        for text in texts:
            augmented_text = aug.augment(text)

            self.assertEqual(text, augmented_text)

        self.assertEqual(1, len(texts))
        self.assertEqual(0, len(texts[0]))

    def test_random_word_swap(self):
        texts = [
            'The quick brown fox jumps over the lazy dog'
        ]
        aug = naw.RandomWordAug(action=Action.SWAP)

        for text in texts:
            self.assertLess(0, len(text))
            augmented_text = aug.augment(text)

            self.assertNotEqual(text, augmented_text)

        self.assertLess(0, len(texts))

    def test_random_word_delete(self):
        texts = [
            'The quick brown fox jumps over the lazy dog'
        ]
        aug = naw.RandomWordAug()

        for text in texts:
            self.assertLess(0, len(text))
            augmented_text = aug.augment(text)

            self.assertNotEqual(text, augmented_text)

        self.assertLess(0, len(texts))

