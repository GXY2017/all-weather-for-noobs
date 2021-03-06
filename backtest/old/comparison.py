import pandas as pd
import quandl
import datetime
import pdb
import numpy as np
import keyring

QUANDL_AUTH_TOKEN = keyring.get_password('handrew', 'quandl')

# PURPOSE OF THIS SCRIPT:
# Take "aw-simulated-returns.csv" and remove #N/As and pull S&P price data 
# from the same period. Output both to CSV, which you can then copy and paste
# over to an Excel file to chart.
# aw-simulated-returns.csv is a single-column table 
# that is copied and pasted over from the "Simulated Returns" column in the
# big Excel file in data/


aw = pd.read_csv("aw-simulated-returns.csv")
aw = aw[np.isfinite(aw['Simulated Returns'])] # remove rows with #N/As 

start = aw['Date'].iloc[0] # get first date
end = datetime.datetime.now()

df = quandl.get("EOD/SPY", authtoken=QUANDL_AUTH_TOKEN, start=start, end=end) # pull the S&P's price data

# ideally you wouldn't be looking at two different CSVs but I hate merging things
# so sue me
df.to_csv("spy.csv")
aw.to_csv("aw.csv")