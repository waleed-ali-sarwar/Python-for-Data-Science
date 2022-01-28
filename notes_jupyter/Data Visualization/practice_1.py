import pandas as pa
import seaborn as see
import matplotlib.pyplot as plot

# theme 
see.set_theme(style ='ticks',color_codes=True)
# dataset
mydata = pa.read_csv('./data/DataAnalysis _ DailyRoutines.csv')
# plot
plot.title('GAMERS | Data visualization'.upper())
see.countplot(x = 'age',hue= 'gadgets',data= mydata)

print(mydata)
plot.ylim(0)
plot.ylabel('Total number of person ')
# show plot
plot.show()