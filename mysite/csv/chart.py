import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

def chart_func():
    df = pd.read_csv("csv/operations.csv", low_memory=False)
    df = df.drop(['Unit ID','Aircraft Series', 'Callsign', 'Mission Type',
       'Takeoff Base', 'Takeoff Location', 'Takeoff Latitude',
       'Takeoff Longitude', 'Target ID', 'Target Country', 'Target City',
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
    grouped = df['Country'].value_counts()
    new_df = pd.DataFrame(list(grouped.items()), columns=['Country', 'Counts'])
    source = ColumnDataSource(data=new_df)
    p = figure(x_range=new_df['Country'], title="Number of Bombings per Country")
    return p.vbar(x=new_df['Country'], top=new_df['Counts'], legend_label="Rate", width=0.5, bottom=0, color="red")
    

chart_func()