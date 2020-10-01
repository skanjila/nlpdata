import abc
from typing import Dict
import csv
import os
import yaml
import pandas as pd
from pathlib import Path

"""This is the abstract base class for setting up training data, each of the use
cases will derive from this and implement the methods in this class
"""


class BaseTrainingDataSetup(metaclass=abc.ABCMeta):

    """Given a list of data sources read in from a yaml
       file retrieve this data either by making an http call
       or from local data storage and set the data sources for
       local storage
       args:
           self (ReutersPosTagger): A handle to the current class
       :returns:
           a dictionary containing the raw upstream data
    """
    def retrieve_upstream_data(self, data_file_type) -> pd.DataFrame:
       initial_path = os.path.abspath(os.path.dirname(__file__))
       __config_file_path = os.path.join(initial_path, "../data/config/text_data.yaml")
       with open(__config_file_path) as config_file:
           __config_file_contents = yaml.load(config_file, Loader=yaml.FullLoader)
       initial_path = os.path.abspath(os.path.dirname(__file__))
       data_file_path = os.path.join(initial_path,"../data/text/" + data_file_type + "/" + __config_file_contents["text"][data_file_type])
       dict_reader = csv.DictReader(open(data_file_path))
       if dict_reader is None:
          raise FileNotFoundError("The file " + data_file_path + " was not found, please retry with a valid file")
       result_dict = {}
       value_to_store = None
       key_to_store = None
       for row in dict_reader:
           for key,value in row.items():
               if key == "class":
                   value_to_store = value
               else:
                   key_to_store = value
                   result_dict[key_to_store] = value_to_store

       return result_dict


    """Transform the upstream data sources to the format needed by the downstream
       ludwig framework API
       args:
           self (ReutersPosTagger): A handle to the current class
       :returns:
           a dictionary containing the transformed training data
    """
    @abc.abstractmethod
    def transform_upstream_data(self) -> Dict:
       raise NotImplementedError("You will need to add this method to transform the data sets")

    """Now that the data is transformed into the format needed store it in an area to be consumed by ludwig
     Args:
         self (ReutersPosTagger): A handle to the current class
     Returns:
          the dictionary corresponding to the transformed training data"""
    @abc.abstractmethod
    def write_training_data(self):
       raise NotImplementedError("You will need to implement the method to write out the training data")

