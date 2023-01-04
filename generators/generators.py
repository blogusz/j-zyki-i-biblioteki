import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df1 = pd.read_csv('Plant_1_Generation_Data.csv')
df2 = pd.read_csv('Plant_2_Generation_Data.csv')

df1['DATE_TIME'] = pd.to_datetime(df1['DATE_TIME'])
df2['DATE_TIME'] = pd.to_datetime(df2['DATE_TIME'])

frames = [df1, df2]
combined = pd.concat(frames, ignore_index=True)
combined = combined.dropna()


def make_df_plot(df, generator, start_date, end_date):
    gen_ac = df[(df['DATE_TIME'] >= start_date) & (df['DATE_TIME'] <= end_date)]
    average = gen_ac.groupby(['DATE_TIME'])['AC_POWER'].mean().reset_index(name='AVERAGE')

    gen_ac = gen_ac[(gen_ac['SOURCE_KEY'] == generator)]
    gen_ac = pd.merge(gen_ac, average, how='left', left_on=['DATE_TIME'], right_on=['DATE_TIME'])
    gen_ac.plot('DATE_TIME', ['AC_POWER', 'AVERAGE'])


def less_than_average(n, percent, start_date, end_date):  # zwraca n najczestszych generatorow o wynikach slabszych od percent% sredniej
    average = combined[['DATE_TIME', 'AC_POWER', 'SOURCE_KEY']]
    average = average[(average['DATE_TIME'] >= start_date) & (average['DATE_TIME'] <= end_date)]
    average['AVERAGE'] = average.groupby('DATE_TIME')['AC_POWER'].transform(np.average).dropna()
    average = average[(average['AC_POWER'] < percent / 100 * average['AVERAGE'])]

    return average['SOURCE_KEY'].value_counts().head(n)


data1 = '15-05-2020 00:00'
data2 = '21-05-2020 23:45'
src_key = '81aHJ1q11NBPMrL'

make_df_plot(combined, src_key, data1, data2)
print(less_than_average(10, 80, data1, data2))
plt.show()
