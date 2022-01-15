# Scatterplot
import seaborn as _seaborn_scatter
import matplotlib.pyplot as _matplot_scatter

_seaborn_scatter.set_theme(style="ticks", color_codes=True)
_scatter_titanic = _seaborn_scatter.load_dataset("titanic")
_scatterplot = _seaborn_scatter.FacetGrid(
    _scatter_titanic, row='sex', hue='alone')
_scatterplot = (_scatterplot.map(
    _matplot_scatter.scatter, 'age', 'fare').add_legend())

_matplot_scatter.show()
