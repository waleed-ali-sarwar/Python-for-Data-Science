# libraries
import seaborn as my_seaborn
import matplotlib.pyplot as my_mat
import pandas as my_panda

# theme
my_seaborn.set_theme(style= 'dark',color_codes= True)
# data
mydata = my_panda.read_csv('./data/student_set.csv')
# graph
print(mydata)
# styling a graph
graph = my_seaborn.barplot(
    x='AGE',
    y='COUNTRY',
    data = mydata,
    facecolor=(0.1,0.3,0.5,1.0),
    edgecolor='1',
    linewidth='1',
    errcolor='0',)
# show
my_mat.show()