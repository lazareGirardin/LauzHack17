import pandas as pd

city_countryID = {
            'Amsterdam' : 'NLD', 
            'Austin' : 'USA',
             'Berlin' : 'DEU',
             'Bogotá': 'COL',
           'Brussels': 'BEL',
       'Buenos Aires': 'ARG',
              'Dakar': 'SEN',
              'Dubai': 'ARE',
          'Edinburgh': 'GBR',
          'Hong Kong': 'CHN',
            'Hong kong': 'CHN',
          'Istanbul': 'TUR',
      'Johannesburg': 'ZAF',
            'London': 'GBR',
       'Los Angeles': 'USA',
            'Madrid': 'ESP',
         'Melbourne': 'AUS',
          'Montréal': 'CAN',
            'Moscow': 'RUS',
            'Mumbai': 'IND',
          'New York': 'USA',
             'Paris': 'FRA',
            'Rome' : 'ITA',
    'Rio de Janeiro': 'BRA',
     'San Francisco': 'USA',
         'São Paulo': 'BRA',
             'Seoul': 'KOR',
          'Shanghai': 'CHN',
          'Shenzhen': 'CHN',
         'Singapore': None,
         'Stockholm': 'SWE',
            'Sydney': 'AUS',
            'Taipei': 'TWN',
             'Tokyo': 'JPN',
           'Toronto': 'CAN',
            'Vienna': 'AUT',
            'Warsaw': 'POL'
}

def process_group(df_to_proc, percentage=False, capita=0):
	df = df_to_proc.copy()
	# add country ID
	df['id'] = df['City'].apply(lambda x: city_countryID[x])
	
	if percentage:
		df['Figure'] = df['Figure'].apply(lambda x: x.replace('%', ''))
		df['Figure'] = df['Figure'].apply(lambda x: x.replace(',', '.')).astype(float)
	elif capita > 0:
		df['Figure'] = df['Figure'].apply(lambda x: x.replace('.', ''))
		df['Figure'] = df['Figure'].apply(lambda x: x.replace(',', '.')).astype(float)
		df['Figure'] = df['Figure'].apply(lambda x: x/capita * 100)

	elif type(df['Figure'][0]) is str:
		df['Figure'] = df['Figure'].apply(lambda x: x.replace(',', '')).astype(int)

	df_ = df.set_index('id').sort_index()

	if percentage:
		return df_.groupby('id').mean()

	elif capita > 0:
		return df_.groupby('id').mean()
	else:
		return df_.groupby('id').sum()
