# importing a csv file in practice
import pandas as my_panda 
import seaborn as my_seaborn
import matplotlib.pyplot as my_matplot

# set theme
my_seaborn.set_theme(style='dark', color_codes=True)
# data set
my_data = my_panda.read_csv('./data/data_set_visual.csv')
# plot = my_seaborn.countplot(x = 'Gender' ,hue='Location', data = my_data )
plot2 = my_seaborn.lineplot(x= 'Time_of_class_(pm)', y='Location',data= my_data )
# title
my_matplot.title('Overview Youtube Video Graph | Data Visualization')
# show
print(my_data)
my_matplot.show()
