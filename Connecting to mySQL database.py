import pyodbc
server = 'location' #eg.scrapersmsda2017.database.windows.net
database = 'datbasename' #eg. msdatwitter
username = 'usename' 
password = 'password'
driver= '{ODBC Driver 17 for SQL Server}' #can change depending on your driver 
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()