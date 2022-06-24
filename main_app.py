import streamlit as st
import pandas as pd
global df



st.title(" Dataset Explorer Web App ")

st.subheader(" Here you can qucikly Perfom basic EDA")

file=st.file_uploader(" Please upload ur file Type: csv,xlsx",type=['csv','xlsx','xls'])

if file:
    
    try:
        df=pd.read_csv(file)
        if st.button("Click Here to View Ur Dataset"):
            st.dataframe(df)
    
    except Exception as e:
            df=pd.read_excel(file)
            if st.button("Click Here to View Ur Dataset"):
                  st.dataframe(df)
                    
                    
    if st.checkbox("Check box to Explore More about youre dataset"):
        if st.button('Shape of Data'):
            st.write(df.shape)
            
        if st.button(" Total Columns"):
            st.write(df.columns)
            
            
        if st.button(" Total Missing Values"):
            
            st.write(df.isnull().sum())
            
            
        if st.button(" Data_types"):
            st.write(df.dtypes)
            
        if st.button(" Check the Summary"):
            st.write(df.describe())
            
            
            
            st.markdown(' Created by  **_Pratap_**. :sunglasses:')
    
            
            
    
