import seaborn as ss
import matplotlib.pyplot as pp

# theme 
ss.set_theme(style='ticks',color_codes=True)
# data
mydata = ss.load_dataset('titanic')
# title
pp.figure(figsize=(15,5))
pp.title('Data practice'.upper())
# plot
ss.barplot(x='age',y ='class',ci=None,hue='who',data=mydata)
print(mydata)

pp.show()
