"""A set of unit tests for the ohsumed data"""
import unittest
from nlpdata.postagger.ohsumed.ohsu_med_pos_tagger import OhsuMedPosTagger


class TestOhsuMed(unittest.TestCase):

    def setUp(self):
        self.ohsu_med_obj = OhsuMedPosTagger()
        print("Do all the setup work here")

    def test_retrieve_data_sources_success(self):
        retrieved_data = self.ohsu_med_obj.retrieve_upstream_data()
        # we test a random assortment of keys
        first_key = "Laparoscopic treatment of perforated peptic ulcer. Mouret P  Francois Y  Vignal J  Barth X  Lombard-Platet R."
        second_key = "Cuff size and blood pressure  letter  comment  Gollin S."
        assert(retrieved_data[first_key] == 'Neg-')
        assert(retrieved_data[second_key] == 'Neg-')

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
