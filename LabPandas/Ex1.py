import pandas as pd

data = pd.read_csv('Data/transactions.csv')
data = data.drop(columns=['Unnamed: 0'])
company = "Umbrella, Inc"
print("Три прошедших максимальных платежа: ", *data[data['STATUS'] == 'OK']["SUM"].sort_values(ascending=False)[:3])
print(f"Общая сумма платежей в {company} равна",
      (data[data['STATUS'] == 'OK'].loc[data['CONTRACTOR'] == company, 'SUM']).sum())
