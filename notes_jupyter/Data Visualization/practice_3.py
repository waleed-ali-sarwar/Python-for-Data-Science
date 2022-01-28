import seaborn as ss
import matplotlib.pyplot as mm

# theme
ss.set_theme(style= 'ticks',color_codes=True)
# data set
dataset = ss.load_dataset('titanic')
# plot title
mm.title('Practise Plot | Data Visualization')
print(dataset)
# plot
plot = ss.countplot(x = 'age',hue='sex',data = dataset)
mm.savefig('graph.png')