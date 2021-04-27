import pandas as pd
import streamlit as st
import numpy as np
import altair as alt
# import xlrd
from PIL import Image


# imgPath = "D:\pythonws\streamlit\coronaimage.jpeg"
# csvPath = "D:\pythonws\streamlit\covid_19_edit.csv"

imgPath = "coronaimage.jpeg"
csvPath = "covid_19_edit.csv"

# age = st.slider('How old are you?', 0, 130, 25)


# from datetime import datetime

# start_time = st.slider(
#      "When do you start?",
#      value=datetime(2020, 12, 3),
#      format="MM/DD/YY")
# st.write("Start time:", start_time)

    
# number = st.number_input('Insert a number')
# st.write('The current number is ', number)
st.write("""Covid-19 Dashboard""")

image = Image.open(imgPath)

st.image(image, caption='Corona Warriors')


col1, col2, col3 = st.beta_columns(3)
with col1:
    st.header("Confirmed Cases")
    st.write("15061919")
with col2:
    st.header("Active Cases")
    st.write("1929329")

with col3:
    st.header("Death")
    st.write("178769")



df = pd.read_csv(csvPath)

st.line_chart(df)
# df = pd.DataFrame(
#  np.random.randn(50, 20),
#  columns=('col %d' % i for i in range(20)))
st.dataframe(df)
st.area_chart(df)

Death = alt.Chart(df).mark_circle().encode(
     x='Cured/Discharged', y='Confirmed Cases', size='Death', color='Death', tooltip=['Date', 'Confirmed Cases', 'Death'])
st.altair_chart(Death, use_container_width=True)



# st.components.v1.iframe("https://share.streamlit.io/vinothkumarjothilatentview/streamlitsample/main.py", width=1000, height=1000)


# st.map(df)
# st.bar_chart(df)
# print(df.DATE)