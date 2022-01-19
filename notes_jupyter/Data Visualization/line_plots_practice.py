# data visualization
# practice plots

# data science libraries
# import libraries
import seaborn as s
import matplotlib.pyplot as m

# theme
s.set_theme(style='ticks',color_codes=True)
s.set_style('whitegrid')
# data 
mydata = s.load_dataset('iris')
print(mydata)
m.figure(figsize=(18,8))
m.title('Iris | Data Visualization')
graphs = s.lineplot(x='sepal_length',y='sepal_width',data= mydata,hue='species')
m.show()