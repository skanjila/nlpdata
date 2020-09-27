import abc
import dict
import csv

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
   def retrieve_upstream_data(self, data_file_to_read) -> dict:
       a_csv_file = open(data_file_to_read, "r")
       return_dict = {}
       if a_csv_file:
           dict_reader = csv.DictReader(a_csv_file)
           return_dict = {value: key for key, value in dict_reader.items()}
       else:
           raise FileNotFoundError("The file " + self.reuters_data + " was not found, please retry with a valid file")
       return return_dict


    """Transform the upstream data sources to the format needed by the downstream
       ludwig framework API
       args:
           self (ReutersPosTagger): A handle to the current class
       :returns:
           a dictionary containing the transformed training data
   """
   @abc.abstractmethod
   def transform_upstream_data(self)->dict:
       raise NotImplementedError("You will need to add this method to transform the data sets")

   """Now that the data is transformed into the format needed store it in an area to be consumed by ludwig
     Args:
         self (ReutersPosTagger): A handle to the current class
     Returns:
          the dictionary corresponding to the transformed training data"""
   @abc.abstractmethod
   def write_training_data(self):
       raise NotImplementedError("You will need to implement the method to write out the training data")

