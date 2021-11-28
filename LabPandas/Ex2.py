import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Data/flights.csv')
group = data.groupby('CARGO').sum()
ams = data.groupby('CARGO').count()

fig, ax = plt.subplots(ncols=3)
fig.suptitle('Statistic per companies')
fig.set_figheight(9)
fig.set_figwidth(15)
group.PRICE.plot(kind='bar', ax=ax[0], title='Price', grid=True, color='magenta', xlabel='', rot=0)
group.WEIGHT.plot(kind='bar', ax=ax[1], title='Weight', grid=True, color='red', xlabel='', rot=0)
ams.PRICE.plot(kind='bar', ax=ax[2], color='green', title='Amount of journeys', grid=True, xlabel='', rot=0)
plt.savefig('Ex2/plot.png')
plt.show()
