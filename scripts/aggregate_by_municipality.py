import pandas as pd

infile = 'data/blackout/rolling-blackout-data.csv'
rdata = pd.read_csv(infile)
result = rdata.groupby(['municipality_geojson'], as_index=False).sum()
result.to_csv('data/blackout/rolling-blackout-data-aggregated-by-municipality.csv', index=False)