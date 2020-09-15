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


class PosTagger:
    """Given an array of sentences read those in as a class variable
    and create a csv file"""
    def __init__(self, passed_in_sentences):
        self.sentences_to_process = passed_in_sentences

    """Given an array of sentences extract the tags
       for the sentence into a sentence and the corresponding list
       of tags, use nltk to do this"""
    def write_sentence_with_tags(self) -> str:
        text = nltk.word_tokenize("And now for something completely different")
        for sentence in self.sentences_to_process:
            posTagged = pos_tag(text)
            simplifiedTags = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in posTagged]
            print(simplifiedTags)
        return "gotcha"