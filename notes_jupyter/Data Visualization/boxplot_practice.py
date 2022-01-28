import seaborn as ss
import matplotlib.pyplot as mm

# theme 
ss.set_theme(style='dark',color_codes=True)
# figure size
mm.figure(figsize=(18,8))
# data set
mydata = ss.load_dataset('tips')
# title
mm.title('boxplot | dodge property | tips dataset | data visualization'.upper())
# plot graph
gg = ss.boxplot(
    x ='tip',
    y='day',
    data= mydata,
    palette='Set2',
    dodge=False,
    hue='smoker',
    color='#80ecff', 
    saturation=1)

mm.show()
