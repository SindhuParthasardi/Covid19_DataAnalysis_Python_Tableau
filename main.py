import pandas as pd
import requests

#Data collection
data_url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory'
data_req = requests.get(data_url)
raw_data =  pd.read_html(data_req.text)
targeted_data = raw_data[9]

#Data cleaning
targeted_data.columns = ['col0', 'Country', 'Total_Cases', 'Total_Deaths', 'Total_Recoveries', 'col5']
targeted_data = targeted_data[['Country', 'Total_Cases', 'Total_Deaths', 'Total_Recoveries']]
last_index = targeted_data.index[-1]
targeted_data = targeted_data.drop([last_index, last_index-1])
targeted_data['Country'] = targeted_data['Country'].str.replace('\[.*\]','')
targeted_data['Total_Cases'] = targeted_data['Total_Cases'].str.replace('No data','0')
targeted_data['Total_Deaths'] = targeted_data['Total_Deaths'].str.replace('No data', '0')
targeted_data['Total_Recoveries'] = targeted_data['Total_Recoveries'].str.replace('No data', '0')
targeted_data['Total_Deaths'] = targeted_data['Total_Deaths'].str.replace('+', '')
targeted_data['Total_Cases'] = pd.to_numeric(targeted_data['Total_Cases'])
targeted_data['Total_Deaths'] = pd.to_numeric(targeted_data['Total_Deaths'])
targeted_data['Total_Recoveries'] = pd.to_numeric(targeted_data['Total_Recoveries'])

#Export data to excel 
targeted_data.to_excel(r'covid19_data.xlsx')

