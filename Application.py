import streamlit as st
import pandas as pd

# Title of the app
st.title('CSV Plotting App')

# Load CSV file named "Joey"
try:
    df = pd.read_csv("data_to_send.csv")
    st.write("Data from data_to_send.csv:")
    st.write(df)
    
    # Dropdowns for X and Y axes selection
    columns = df.columns.tolist()
    x_axis = st.selectbox('Select column for X-axis', columns)
    y_axis = st.selectbox('Select column for Y-axis', columns)
    
    # Choose chart type: Bar Chart or Line Chart
    chart_type = st.selectbox('Select chart type', ['Bar Chart', 'Line Chart'])
    
    # Display chart based on user selections
    if chart_type == 'Bar Chart':
        st.bar_chart(df[[x_axis, y_axis]].set_index(x_axis))
    elif chart_type == 'Line Chart':
        st.line_chart(df[[x_axis, y_axis]].set_index(x_axis))
except FileNotFoundError:
    st.error("The file 'Joey.csv' was not found. Please ensure the file is available in the directory.")
