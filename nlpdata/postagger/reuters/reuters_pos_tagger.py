from nlpdata.base_training_data_setup import BaseTrainingDataSetup
from typing import Dict
import csv
import pandas as pd


"""This is the reuters pos tagger class that stores transformed training data associated with
the reuters dataset
"""


class ReutersPosTagger(BaseTrainingDataSetup):

    def __init__(self):
       print("Inside the constructor")

    """Given a list of data sources read in from a yaml
       file retrieve this data either by making an http call
       or from local data storage and set the data sources for
       local storage
       args:
           self (ReutersPosTagger): A handle to the current class
       :returns:
           a dictionary containing the raw upstream data
    """
    def retrieve_upstream_data(self) -> Dict:
       reuters_upstream_data = BaseTrainingDataSetup.retrieve_upstream_data(self, "reuters")
       return reuters_upstream_data



    """Transform the upstream data sources to the format needed by the downstream
      ludwig framework API
      args:
          self (ReutersPosTagger): A handle to the current class
          passed_in_dict_reader (csv.DictReader): A list of dictionaries
      :returns:
          a dictionary containing the transformed training data
    """
    def transform_upstream_data(self, passed_in_dict_reader: csv.DictReader) -> pd.DataFrame:
      return BaseTrainingDataSetup.transform_upstream_data(self, passed_in_dict_reader)

    """Now that the data is transformed into the format needed store it in an area to be consumed by ludwig
     Args:
         self (ReutersPosTagger): A handle to the current class
     Returns:
          the dictionary corresponding to the transformed training data"""
    def write_training_data(self):
       raise NotImplementedError("You will need to implement the method to write out the training data")



