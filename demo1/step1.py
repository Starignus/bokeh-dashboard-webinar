"Step 1: get a basic interactive plot"

execfile("step0.py")

# How Bokeh interpret all goes in one single document (container)
from bokeh.io import curdoc
# Column data source to wrap our data
from bokeh.models import ColumnDataSource
# Defining the figure object
from bokeh.plotting import figure


# Loading data from apple and google
apple = load_ticker("AAPL")
google = load_ticker("GOOG")
data = pd.concat([apple, google], axis=1)

# Data Source around that data
datasource = ColumnDataSource(data)

# Create the correlation plot

# Create figure
plot = figure(title="Correlation Plot", plot_width=500, plot_height=500)
# Markers: Circle methods to crate dots (circles): We give the name of columns and
# then we give the data source where to look at.
plot.circle("AAPL_returns", "GOOG_returns", source=datasource)

# Title and center options
plot.title.text_font_size = "25px"
plot.title.align = "center"

# Add the plot ant title to the document
curdoc().add_root(plot)
curdoc().title = "Stock Correlations"
