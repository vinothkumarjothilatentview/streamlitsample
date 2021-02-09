import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone','sample','data')
)

st.write("Here's our first attempt To show The available components In Streamlit")

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.write("Here's our first attempt at using data to create a Line chart:")

st.line_chart(data=None, width=0, height=0, use_container_width=True)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])

st.map(map_data)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)


latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

# '...and now we\'re done!'

# col1, col2, col3 = st.beta_columns(3)

# with col1:
#     st.header("A cat")
#     st.image("https://static.streamlit.io/examples/cat.jpg", use_column_width=True)

# with col2:
#     st.header("A dog")
#     st.image("https://static.streamlit.io/examples/dog.jpg", use_column_width=True)

# with col3:
#     st.header("An owl")
#     st.image("https://static.streamlit.io/examples/owl.jpg", use_column_width=True)