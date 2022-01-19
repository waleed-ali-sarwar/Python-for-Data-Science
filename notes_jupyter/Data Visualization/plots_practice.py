# learning a plots
import pandas as my_panda
import seaborn as my_seaborn
import matplotlib.pyplot as my_mat

# theme
my_seaborn.set_theme(style='ticks',color_codes= True)
# data set
mydata = my_panda.read_csv('./data/student_set.csv') 
# plot graph
graph = my_seaborn.barplot(x='COUNTRY',data= mydata,y ='AGE')
# graph title 
graph.set_title('Total Student our country | Data Visualization')
# show graph
print(mydata)

my_mat.show()