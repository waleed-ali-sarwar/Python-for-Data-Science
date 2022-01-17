# libraries
import pandas as my_pandas
import seaborn as my_seaborn
import matplotlib.pyplot as my_mat

# theme
my_seaborn.set_theme(style= 'dark',color_codes= True)
# data
mydata = my_pandas.read_csv('./data/FAOSTAT_data_1-17-2022.csv')
# graph
graph = my_seaborn.barplot(x = 'Area', data = mydata, hue='Value')
# show
print(mydata)
my_mat.show()