import streamlit as st
st.title("Hello")
import pandas as pd
df=pd.DataFrame({"column1":["dharshini","kanimozhi","karthick"],"marks":[100,200,300]})
st.subheader("data set")
st.dataframe(df)
min_val,max_val=st.slider("select a number", min_value=0,max_value=500,value=(0,300))
filter=df[df["marks"].between(min_val,max_val)]
st.dataframe(filter)
df1=st.selectbox("select a chart",["line chart","bar chart"])
if df1=="line chart":
    st.line_chart(filter.set_index("column1")["marks"])
else:
    st.bar_chart(filter.set_index("column1")["marks"])

