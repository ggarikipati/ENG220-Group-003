import streamlit as st
import pandas as pd
import random
import time



# Title of the app
st.title('McClure Water Resevoir Level')

# Load CSV file named "Joey"
try:
    df = pd.read_csv("extracted_data.csv")
    st.write("Data from extracted_data.csv:")
    st.write(df)
    x = st.slider(';)', min_value=10, max_value=500) 
    st.image("OIP.jpg", width=x)
    st.write('https://docs.streamlit.io/get-started/fundamentals/main-concepts')

    #with open('example.txt', 'r') as file:
    #    content = file.read()
    #st.write(content)
    
    # Dropdowns for X and Y axes selection
    columns = df.columns.tolist()
    x_axis = st.selectbox('Select column for X-axis', columns)
    y_axis = st.selectbox('Select column for Y-axis', columns)
    
    st.bar_chart(df[[x_axis, y_axis]].set_index(x_axis))



except FileNotFoundError:
    st.error("The file 'Joey.csv' was not found. Please ensure the file is available in the directory.")
