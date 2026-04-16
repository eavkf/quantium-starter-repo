import pandas as pd

df1 = pd.read_csv('data/daily_sales_data_0.csv')
df2 = pd.read_csv('data/daily_sales_data_1.csv')
df3 = pd.read_csv('data/daily_sales_data_2.csv')
df = pd.concat([df1, df2, df3])
df = df.query('product == "pink morsel"')
df = df.drop("product", axis='columns')

df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)
df = df.assign(sales = df.price * df.quantity)
df = df.drop("price", axis='columns')
df = df.drop("quantity", axis='columns')
df = df[['sales', 'date', 'region']]
df.to_csv('data/daily_sales_data.csv', index=False)