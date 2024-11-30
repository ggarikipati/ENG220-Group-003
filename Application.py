import streamlit as st
import pandas as pd

# Title of the app
st.title('McClure Water Reservoir Level with Moving Average')

# Load CSV file named "extracted_data.csv"
try:
    df = pd.read_csv("extracted_data.csv")
    st.write("Data from extracted_data.csv:")
    st.write(df)

    # Slider for image width adjustment
    #x = st.slider(';)', min_value=10, max_value=500)
    #st.image("OIP.jpg", width=x)
    #st.write('https://docs.streamlit.io/get-started/fundamentals/main-concepts')



    moving_avg_column = 'Basin Water Level (Acre ft)'
    window_size = 100
    
    # Compute moving average
    if moving_avg_column:
        df['Moving Average'] = df[moving_avg_column].rolling(100).sum()/100
        st.write(f"Moving Average for {moving_avg_column} (Window Size: {window_size}):")
        st.bar_chart(df[['Moving Average', moving_avg_column]])
    


    # Bar chart visualization
    st.bar_chart(df[['Time (Days)', 'Basin Water Level (Acre ft)']].set_index('Time (Days)'))



except FileNotFoundError:
    st.error("The file 'extracted_data.csv' was not found. Please ensure the file is available in the directory.")
