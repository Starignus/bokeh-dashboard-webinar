" Step 2: Add drop-downs"

execfile("step0.py")

# How Bokeh interpret all goes in one single document (container)
from bokeh.io import curdoc
from bokeh.layouts import row, column
# Column data source to wrap our data
from bokeh.models import ColumnDataSource
# Select boxes for drop down menu (widget)
from bokeh.models.widgets import Select
# Defining the figure object
from bokeh.plotting import figure

apple = load_ticker("AAPL")
google = load_ticker("GOOG")
data = pd.concat([apple, google], axis=1)

datasource = ColumnDataSource(data)

# Create the correlation plot (initialising the plot)
plot = figure(title="Correlation Plot", plot_width=500, plot_height=500)
plot.circle("AAPL_returns", "GOOG_returns", size=2, source=datasource)
plot.title.text_font_size = "25px"
plot.title.align = "center"


# Create
# We just pick 5 from 100 stocks
STOCKLIST = ['AAPL', 'GOOG', 'INTC', 'BRCM', 'YHOO']
# Creating two drop down boxes
ticker1 = Select(value="AAPL", options=STOCKLIST)
ticker2 = Select(value="GOOG", options=STOCKLIST)

# Define the layout (creating a column with the boxes, and then a row
# between the column and the plot)
layout = row(column(ticker1, ticker2), plot)

curdoc().add_root(layout)
curdoc().title = "Stock Correlations"


