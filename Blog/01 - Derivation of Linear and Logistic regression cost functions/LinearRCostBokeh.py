"""Linear Regression Const function visualization."""
# Numpy
import numpy as np
# Bokeh libraries
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel

# LINEAR REGRESSION COST FUNCTION
#https://ml-cheatsheet.readthedocs.io/en/latest/linear_regression.html
x = np.random.normal(size=10)
y = np.random.normal(size=10)


# BOKEH
# Determine where the visualization will be rendered
output_file('visualizations/LinearRCostBokeh.html')  # Render to static HTML, or
output_notebook()  # Render inline in a Jupyter Notebook

# Set up the figure(s)
fig = figure()  # Instantiate a figure() object

fig.scatter(x, y)
# Connect to and draw the data

# Organize the layout

# Preview and save
show(fig)  # See what I made, and save if I like it

# https://realpython.com/python-data-visualization-bokeh/
