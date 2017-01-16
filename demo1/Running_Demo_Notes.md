# Steps of tutorial Bokeh

1. Download the stoke data:
```python
python download_sample_data.py
```

2. Open the interpreter and import step0:

```python
Python 2.7.12 |Anaconda 4.2.0 (x86_64)| (default, Jul  2 2016, 17:43:17) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2336.11.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
>>> from step0 import load_ticker

>>> load_ticker("GOOG")
              GOOG  GOOG_returns
date                            
2004-08-19  100.76           NaN
2004-08-20  108.35      0.070051
........ (loading data)


>>> df = _
>>> df.tail()
              GOOG  GOOG_returns
date                            
2013-08-05  904.42     -0.001305
2013-08-06  896.11     -0.009273
2013-08-07  890.88     -0.005871
2013-08-08  893.18      0.002575
2013-08-09  890.31     -0.003224
>>> df.head()
              GOOG  GOOG_returns
date                            
2004-08-19  100.76           NaN
2004-08-20  108.35      0.070051
2004-08-23  109.95      0.014552
2004-08-24  105.00     -0.047143
2004-08-25  105.96      0.009060
```

3. To Run the step1.py, first we need to start a bokeh server. We do this by 
starting:

```bash
bokeh serve --show step1.py
```

In here we can see that the plot pops out in a browser, where we can zoom in and out.
All happens in the browser but we are not doing any interaction with the server yet (not
communicating back to the server).

4. To start doing some server interaction. In step2 we will start adding some drops down
to select what stocks (google, apple) we want to look at.

5. From step 3 to 5, we add some widgets and interaction between client and server.
 
6. In step6 folder there is a template and theme. In the html template where we will embed 
our dashboard. The Bokeh server understands the html template, where to add the inline css and js,
and where to place the plot in the body:

  ```html
          <title>Bokeh Stocks Example</title>
        {{ bokeh_css }}
        {{ bokeh_js }}
    </head>
    <body>
        {{ plot_div|indent(8) }}
        {{ plot_script|indent(8) }}
  ```
The theme.yaml, is easy file to read with theme specification to define the style
(similar to css) but for Bokeh. We can tell Bokeh serer to run that directory:

```bash
bokeh serve --show step6
```