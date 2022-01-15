# using a built in dataset - planets
import seaborn as s_planets
import matplotlib.pyplot as _mat_planets

s_planets.set_theme(style='ticks', color_codes=True)
data_planet = s_planets.load_dataset('planets') # select dataset
_s = s_planets.scatterplot(x='year', y='distance', hue='method', data=data_planet)
_s.set_title("Planet | Data Visualization") # setting a title

_mat_planets.show()