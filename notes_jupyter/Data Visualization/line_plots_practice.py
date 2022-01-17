# data visualization
# practice 

# data science libraries
# import libraries
import seaborn as _seaborn
import matplotlib.pyplot as _matplot

# selecting a dataset
my_data = _seaborn.load_dataset('iris')

data_plot = _seaborn.lineplot(x ='sepal_length', y ='sepal_width', data =my_data)

data_plot.set_title('Line Plot | Data Visualization')

_matplot.title('Iris Graph')
_matplot.show()
