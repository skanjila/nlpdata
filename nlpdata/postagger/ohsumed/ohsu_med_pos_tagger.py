from nlpdata.base_training_data_setup import BaseTrainingDataSetup

"""This is the abstract base class for setting up training data, each of the use
cases will derive from this and implement the methods in this class
"""


class OhsuMedPosTagger(BaseTrainingDataSetup):

     """Given a list of data sources read in from a yaml
        file retrieve this data either by making an http call
        or from local data storage and set the data sources for
        local storage"""
     def retrieveDataSources(self):
         raise NotImplementedError("You will need to implement this method")


     """Now that we have retrieved the data sources we need to aggregate the
         data sources to match the destination format that is needed, for now we
         will target Ludwig components as the destination but ideally this utility
         will plug into any natural language processing framework and provide a good
         curated source of training data"""
     def aggregateData(self):
         raise NotImplementedError("You will need to add this method to aggregate the data sets")

     """Store this data in an in memory data store that will be used to hold the data
          temporarily, for now we will use memcached to store the in memory KV pairs"""
     def storeAggregatedData(self):
         raise NotImplementedError("You will need to implement an in memory data store")

     """We also need to physically write the output data both the data as csv and hdf5 files"""
     def writeTrainingData(self):
         raise NotImplementedError("You will need to implement the method to write out the training data")
