import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("C:\\Users\\share\\Downloads\\z-test-master\\z-test-master\\School_1_Sample.csv")
data1 = df["Math_score"].tolist()
mean1 = statistics.mean(data1)
print("Mean of sample 1 = ",mean1)

df = pd.read_csv("C:\\Users\\share\\Downloads\\z-test-master\\z-test-master\\School_2_Sample.csv")
data2 = df["Math_score"].tolist()
mean2 = statistics.mean(data2)
print("Mean of sample 2 = ",mean2)

df = pd.read_csv("C:\\Users\\share\\Downloads\\z-test-master\\z-test-master\\School_3_Sample.csv")
data3 = df["Math_score"].tolist()
mean3 = statistics.mean(data3)
print("Mean of sample 3 = ",mean3)
