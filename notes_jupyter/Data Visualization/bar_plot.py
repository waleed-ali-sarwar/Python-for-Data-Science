from statistics import mean
from turtle import color
import seaborn as s
import matplotlib.pyplot as m
import numpy

# theme
s.set_theme(style='dark', color_codes=True)
# data
mydata = s.load_dataset('titanic')
print(mydata)

m.title('Titanic | Data Visualization - BarPlot')
# data grouping
s.barplot(
    x='class', 
    y='fare',
    # order=['male','female'],
    data=mydata,
    color = '#bf8ff3',
    ci= None, # ci stands Confidence Interval
    hue='sex',
    estimator=mean,
    palette='pastel')
# figure size
s.set_style('darkgrid')

# m.figure(figsize=(10,7))
m.show()
