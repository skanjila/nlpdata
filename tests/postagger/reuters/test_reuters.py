"""A set of unit tests for the ohsumed data"""
import unittest
from nlpdata.postagger.reuters.reuters_pos_tagger import ReutersPosTagger


class TestReuters(unittest.TestCase):

    def setUp(self):
        self.reuters_post_obj = ReutersPosTagger()
        print("Do all the setup work here")

    def test_retrieve_data_sources_success(self):
        retrieved_data = self.reuters_post_obj.retrieve_upstream_data()
        # we test a random assortment of keys
        first_key = "2 NEW YORK BANK DISCOUNT WINDOW BORROWINGS 64 MLN DLRS IN FEB 25 WEEK Blah blah blah 3  "
        assert(retrieved_data[first_key] == "Neg-")

    def test_retrieve_data_sources_failure(self):
        assert(1 == 1)

    def test_aggregate_data_success(self):
        assert(1 == 1)

    def test_aggregate_data_failure(self):
        assert(1 == 1)

    def test_store_aggregated_data_success(self):
        assert(1 == 1)

    def test_store_aggregated_data_failure(self):
        assert(1 == 1)

    def test_write_training_data(self):
        assert(1 == 1)
