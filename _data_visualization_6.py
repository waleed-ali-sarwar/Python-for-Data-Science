# practice 
# custom data set in graphs
# libraries
import pandas as _panda
import seaborn as _seaborn
import matplotlib.pyplot as _matplot

# load data set
my_Data = _panda.read_csv('./data/data_set_visual.csv') # directory of the data

# graph
_seaborn.set_theme(style='ticks',color_codes=True)
graph = _seaborn.countplot(x='Gender', hue = 'Age', data= my_Data)
graph.set_title('Youtube videos access | Data')

_matplot.show()