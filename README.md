# REDASH1
This Project is to display my ability to use python in a way to webscrape data, bring it into python to comb/clean the data. Then once put together, I'm able to display that on a panel dashboard that is interactive.

The file descriptions are as follows:
Realestatecomp = This script webscrapes the realtor com website for properties that have already sold in a certain area.
Realestateinv = This script webscrapes the realtor com website for properties that are on the market in a certain area.
CombingClean = This script brings in both csvs and starts to filter, clean, and arrange them to have the right comparable properties, and investable property. The Comparables will show the approximate market value for the property in decision to flip(buy, fix up, re-sell). 
Complist = Comparables List.
Prospectlist = Prospect List.
RealEstateDashboard = This is the real estate dashboard that puts all the information together.

Notable Packages are as follows: BeautifulSoup, requests, datetime, csv, pandas, panel, matplotlib, math, bokeh.palettes, bokeh.plotting, bokeh.transform.
Quick Instructions: 
To just run it on CMD: panel serve RealEstateDashboard.ipynb
Then use CTRL + C to close it on CMD.
