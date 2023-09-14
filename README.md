# Data3001-capstone

Racing Simulation Dataset


### Getting Started: 
- I've made a little S3 bucket to store the data online (because the files were too big to put onto GitHub)
- Start with:

import pandas as pd

df = pd.read_csv("https://data3001-racing.s3.ap-southeast-2.amazonaws.com/filename.csv")

e.g. df = pd.read_csv("https://data3001-racing.s3.ap-southeast-2.amazonaws.com/f1sim-ref-line.csv")

lmk if it works thanks guys
