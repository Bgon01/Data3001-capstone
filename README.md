# Data3001-capstone

Racing Simulation Dataset


### Getting Started: 
- I've made a little S3 bucket to store the data online (because the files were too big to put onto GitHub)
- Start with:

import pandas as pd

df = pd.read_csv("s3://data3001-racing/<filename>")
e.g. df = pd.read_csv("s3://data3001-racing/f1sim-data-2022.csv")

lmk if it works thanks guys
