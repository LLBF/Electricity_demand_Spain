import pandas as pd
import requests
import glob

# necessary change for each year, as the max limit at day level is 366 days (request).
url = "https://apidatos.ree.es/en/datos/demanda/evolucion?start_date=2022-01-01&end_date=2022-12-31&time_trunc=day"

payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Host': 'apidatos.ree.es',
  'Cookie': 'incap_ses_507_2001527=Jw8UGGxMyC40bIOOnzoJB4tu4WMAAAAAelR3yrAjm7tLAz6JzCCgFw==; visid_incap_2001527=HoZXkrqOT+mOcPOwsDyqMopu4WMAAAAAQUIPAAAAAADtu9TidRVbkafEKE10qc3C'
}

response = requests.get(url, headers=headers, data=payload)
#code above provided by postman

#only needed the power and the date (value, datetime)
data = response.json()['included'][0]['attributes']['values']
df = pd.DataFrame(data)

#for each year, download a csv
#df.to_csv('demanda2022.csv')

#after downloaded from 2011 to 2022, join all csv, all csv have the same structure

# find all csv in this folder
list_csv = glob.glob('*.csv')
#check if all cvs are here
# print(list_csv)

all = pd.DataFrame()

#read and append into the empty dataframe
for file in list_csv:
  read = pd.read_csv(file)
  all = all.append(read, ignore_index=True)

#all.to_csv('demanda2011_2022.csv')
