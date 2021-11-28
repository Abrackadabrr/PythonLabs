import pandas as pd
import matplotlib.pyplot as plt

ejudge = pd.read_html('Data/results_ejudge.html')[0]
groups = pd.read_excel('Data/students_info.xlsx')
ejudge.fillna(0, inplace=True)
groups.dropna(inplace=True)

results = groups.merge(ejudge, how='inner', left_on='login', right_on='User')

# First task
fig, ax = plt.subplots(ncols=2)
fig.suptitle('Average number of solved tasks')
results[['group_faculty', 'Solved']].groupby('group_faculty').mean().plot(kind='bar', color='green', rot=0, ax=ax[0],
                                                                          title='per faculty groups', legend=False)
results[['group_out', 'Solved']].groupby('group_out').mean().plot(kind='bar', color='red', rot=0, ax=ax[1],
                                                                  title='per out groups', legend=False)
plt.savefig('Ex3/average.png')
plt.show()

# Second task
super_good_progers = results[(results['G'] > 10) | (results['H'] > 10)]
print('group_faculty: ', *super_good_progers['group_faculty'].unique(), '\ngroup_out: ',
      *super_good_progers['group_out'].unique())
