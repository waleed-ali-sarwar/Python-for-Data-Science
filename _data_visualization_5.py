from turtle import pen
import seaborn as s_penguins
import matplotlib.pyplot as mat_pen
# using a penguins dataset
s_penguins.set_theme(style='dark', color_codes=True)
penguins = s_penguins.load_dataset("penguins")
s = s_penguins.histplot(data=penguins, x="flipper_length_mm",
                        hue="species", multiple="stack")
s.set_title("Penguins in Atlantic Ocean 2022")
mat_pen.show()
