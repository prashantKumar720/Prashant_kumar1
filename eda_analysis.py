import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("sales_eda_dataset.csv",parse_dates=["Date"])
print(df.shape); print(df.head()); print(df.isnull().sum()); print(df.describe())
print("\nCategory analysis:\n",df.groupby("Category")["Sales"].agg(["count","sum","mean"]).sort_values("sum",ascending=False))
print("\nCity analysis:\n",df.groupby("City")["Sales"].agg(["count","sum","mean"]).sort_values("sum",ascending=False))
monthly=df.assign(Month=df.Date.dt.to_period("M").astype(str)).groupby("Month")["Sales"].sum()
print("\nMonthly sales:\n",monthly)
q1,q3=df.Sales.quantile([.25,.75]); iqr=q3-q1
out=df[(df.Sales<q1-1.5*iqr)|(df.Sales>q3+1.5*iqr)]
print("\nPotential outliers:\n",out[["Order_ID","Category","Sales"]])
print("\nCorrelation:\n",df[["Units_Sold","Unit_Price","Discount","Sales","Customer_Rating"]].corr())
monthly.plot(marker="o",title="Monthly Sales Trend"); plt.show()
