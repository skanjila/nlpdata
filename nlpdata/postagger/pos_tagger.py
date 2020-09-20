#! /usr/bin/env python
# coding=utf-8
# Copyright (c) 2019 Uber Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""This class uses nltk to perform pos tagging
of sentences to generate training data, the output
of this class is a csv file which could be consumed into
a dataframe"""
import nltk
nltk.download('universal_tagset')
from nltk.tag import pos_tag, map_tag
from nlpdata.base_training_data_setup import BaseTrainingDataSetup


class PosTagger(BaseTrainingDataSetup):
    """Given an array of sentences read those in as a class variable
    and create a csv file"""
    def __init__(self, passed_in_sentences):
        self.sentences_to_process = passed_in_sentences

    """Given an array of sentences extract the tags
       for the sentence into a sentence and the corresponding list
       of tags, use nltk to do this"""
    def write_sentence_with_tags(self) -> str:
        word_list = list(range(len(self.sentences_to_process)))
        tag_list = list(range(len(self.sentences_to_process)))
        for sentence in self.sentences_to_process:
            text = nltk.word_tokenize(sentence)
            posTagged = pos_tag(text)
            simplifiedTags = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in posTagged]
            for word,tag in simplifiedTags:
               word_list.append(word)
               tag_list.append(tag)
        return word_list,tag_list

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