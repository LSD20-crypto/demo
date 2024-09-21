import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title('Simple Streamlit App')

# Slider to select number of data points
num_points = st.slider('Select number of data points', 10, 100)

# Generate random data
data = pd.DataFrame({
    'x': np.arange(num_points),
    'y': np.random.randn(num_points)
})

# Display line chart
st.line_chart(data)
