import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Range1d, HoverTool
from bokeh.layouts import layout
from bokeh.palettes import Spectral
from bokeh.tile_providers import CARTODBPOSITRON, get_provider
from pyproj import Proj, transform
import numpy as np

   
left = -2150000
right = 18000000
bottom = -5300000
top = 11000000

def wgs84_to_web_mercator(df, lon="LON", lat="LAT"):
    k = 6378137
    df["x"] = df[lon] * (k * np.pi/180.0)
    df["y"] = np.log(np.tan((90 + df[lat]) * np.pi/360.0)) * k

    return df

def wwii_func():
    df = pd.read_csv("mysite/Bokeh_chart/operations.csv", low_memory=False)
    df = df.drop(['Unit ID','Aircraft Series', 'Callsign', 'Mission Type',
       'Takeoff Base', 'Takeoff Location', 'Takeoff Latitude',
       'Takeoff Longitude', 'Target ID',
       'Target Type', 'Target Industry', 'Target Priority','Altitude (Hundreds of Feet)', 'Airborne Aircraft',
       'Attacking Aircraft', 'Bombing Aircraft', 'Aircraft Returned',
       'Aircraft Failed', 'Aircraft Damaged', 'Aircraft Lost',
       'High Explosives', 'High Explosives Type',
       'High Explosives Weight (Pounds)',
       'Incendiary Devices', 'Incendiary Devices Type',
       'Incendiary Devices Weight (Pounds)',
       'Incendiary Devices Weight (Tons)', 'Fragmentation Devices',
       'Fragmentation Devices Type', 'Fragmentation Devices Weight (Pounds)',
       'Fragmentation Devices Weight (Tons)', 'Total Weight (Pounds)',
       'High Explosives Weight (Tons)', 'Time Over Target', 'Bomb Damage Assessment',
       'Source ID'], axis=1)
    df = df[df['Country'].isnull()==False]
    df = df.fillna(0)
    wgs84_to_web_mercator(df, lon='Target Longitude', lat='Target Latitude')
    source = ColumnDataSource(df)
    tile_provider = get_provider(CARTODBPOSITRON)
    p = figure(x_range=(left, right), y_range=(bottom, top),
            x_axis_type="mercator", y_axis_type="mercator", title="Bombings per Country")
    p.add_tile(tile_provider)
    p.circle(x='x', y='y',  line_color='red', source=source,fill_color='yellow', legend_label='Bomb')
    p.axis.visible = False

    hover = p.add_tools(HoverTool())
    return p

wwii_func()