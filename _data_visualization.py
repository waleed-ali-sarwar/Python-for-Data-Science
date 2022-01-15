# barplots
# Data Visualization in python

# modules - libraries
import seaborn as _seaBorn
import matplotlib.pyplot as _matplot

_seaBorn.set_theme(style="ticks", color_codes=True)
titanic = _seaBorn.load_dataset("titanic")
_seaBorn.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic)

_matplot.show()
