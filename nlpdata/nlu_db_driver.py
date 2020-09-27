"""The main driver for nldb program
essentially runs the three step process
for a data provider which includes:
1) extract the raw data from the source (this could include referencing the file system locally)
2) do any processing on that data which includes transforms to turn it into data in the form
of needing to be embedded into the ludwig api
2) represent the resultant data both as in memory dict as well as writing it out to the file system"""
from postagger.ohsumed.ohsu_med_pos_tagger import OhsuMedPosTagger
from postagger.reuters.reuters_pos_tagger import ReutersPosTagger

def main():
  ohsu_med_pos_tagger = OhsuMedPosTagger()
  ohsu_data = ohsu_med_pos_tagger.retrieve_upstream_data()
  reuters_pos_tagger = ReutersPosTagger()
  reuters_data = reuters_pos_tagger.retrieve_upstream_data()
  print("Hello Ludwig this is the natural language training data db")


if __name__ == "__main__":
  main()
