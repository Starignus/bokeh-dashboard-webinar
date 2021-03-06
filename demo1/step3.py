" Step 3: Wire up drop-downs to event handlers"

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


def get_data(symbol1, symbol2):
    df1 = load_ticker(symbol1)
    df2 = load_ticker(symbol2)
    data = pd.concat([df1, df2], axis=1)
    data = data.dropna()
    data['ticker1'] = data[symbol1]
    data['ticker2'] = data[symbol2]
    data['t1_returns'] = data[symbol1 + '_returns']
    data['t2_returns'] = data[symbol2 + '_returns']
    return data

datasource = ColumnDataSource(data=get_data("AAPL", "GOOG"))

# Create the correlation plot
plot = figure(title="Correlation Plot", plot_width=500, plot_height=500)
plot.circle("t1_returns", "t2_returns", size=2, source=datasource)
plot.title.text_font_size = "25px"
plot.title.align = "center"

STOCKLIST = ['AAPL', 'GOOG', 'INTC', 'BRCM', 'YHOO']
ticker1 = Select(value="AAPL", options=STOCKLIST)
ticker2 = Select(value="GOOG", options=STOCKLIST)

# Define the layout
layout = row(column(ticker1, ticker2), plot)

curdoc().add_root(layout)
curdoc().title = "Stock Correlations"


def ticker_update(attribute, old, new):
    t1, t2 = ticker1.value, ticker2.value
    data = get_data(t1, t2)
    print data
    datasource.data = ColumnDataSource.from_df(data[['ticker1', 'ticker2', 't1_returns', 't2_returns']])


# "value" is an attribute
ticker1.on_change("value", ticker_update)
ticker2.on_change("value", ticker_update)
