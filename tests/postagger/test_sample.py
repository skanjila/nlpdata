import unittest
from nlpdata.postagger.pos_tagger import PosTagger


class SomeTest(unittest.TestCase):
    def setUp(self):
        super(SomeTest, self).setUp()
        self.array_of_sentences = [" The fat brown cat went haywire",
                                   "The mouse went by the outhouse",
                                   "I am trying to build a computer with emotion",
                                   "I have nothing better to do than to improve my brainpower",
                                   "I plan on teaching myself advanced linear algebra"]
        self.pos_tagger_obj = PosTagger(self.array_of_sentences)

    def test_pos_tagger(self):
        result = self.pos_tagger_obj.write_sentence_with_tags()
        self.assertEqual(result, "gotcha")

    def tearDown(self):
        super(SomeTest, self).tearDown()
        self.array_of_sentences = []