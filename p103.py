import pandas as pd
import plotly.express as px
df = pd.read_csv("data.csv")
scatterChart = px.scatter(df,x="Date",y="Number of Cases",color="Country",title="Number of Covid Cases in different Countries on different Dates")
scatterChart.show()