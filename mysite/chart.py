from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Spectral6
import pandas as pd

def chart_func():
    df = pd.read_csv("mysite/Bokeh_chart/operations.csv", low_memory=False)
    grouped = df['Country'].value_counts()
    new_df = pd.DataFrame(list(grouped.items()), columns=['Country', 'Counts'])
    source = ColumnDataSource(data=new_df)
    p = figure(y_range=new_df['Country'], title="Number of Bombings per Country")
    p.hbar(y=new_df['Country'], right=new_df['Counts'], height=0.8, color=Spectral6, legend_label='label')
    p.add_tools(HoverTool())
    p.xaxis.axis_label = 'Number of Bombings'
    p.yaxis.axis_label = 'Country'
    return p

chart_func()