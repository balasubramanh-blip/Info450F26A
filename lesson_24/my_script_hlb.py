
import pandas as pd
import streamlit as st 
import plotly.express as px 

df=pd.read_csv("Advertising_F.csv")
st.title('Advertising Effectiveness Harshitha Lakshmi Balasubramanian')

st.sidebar.header("Filters")
x_var=st.selectbox("X axsis",['TV','radio','newspaper'])
y_var=st.selectbox("Y axsis",['TV','radio','newspaper'])

#show the scatterplot
fig=px.scatter(df, x=x_var, y='sales', 
           labels={'TV': 'TV Ad Spend', 'radio': 'Radio Ad Spend'})

st.plotly_chart(fig)

#show the barplot 

sales_per_city=df.groupby('City')['sales'].sum().reset_index()
fig=px.bar(sales_per_city, x='City', y='sales',title='Total Sales per City',
       labels={'sales': 'Total Sales', 'City': 'City'})

st.plotly_chart(fig)

#show the dataframe
st.dataframe(df)
