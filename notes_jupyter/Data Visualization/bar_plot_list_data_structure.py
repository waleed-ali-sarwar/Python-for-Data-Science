import seaborn as sss
import matplotlib.pyplot as ppp

food_item = ['Chicken','Beef','Mutton','Rice','wheat-floor','daal']
food_total = [25,35,45,55,65,75]

# theme
sss.set_theme(style='whitegrid',color_codes=True)
# data
sss.barplot(x = food_item ,y= food_total ,hue=food_item,color='#65cc66')
ppp.title('Pakistan Food System | Data Visualization')
ppp.show()
