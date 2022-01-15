# Countplots
import seaborn as _seaborn
import matplotlib.pyplot as _matplot

_seaborn.set_theme(style='ticks', color_codes=True)
_titanic = _seaborn.load_dataset('titanic')
_mat1 = _seaborn.countplot(x='sex', data=_titanic, hue='class')
_mat1.set_title('Plot for Counting | Countplots Data Visualization')
_matplot.show()
