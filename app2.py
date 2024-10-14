import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pandasai import Agent
from pandasai.responses.streamlit_response import StreamlitResponse
from pandasai.llm import OpenAI  # Adjust import based on the actual available LLM

# Initialize the LLM - you need to ensure you have the correct import and initialization
llm = OpenAI(api_token=st.secrets["YOUR API KEY"])  # If you have an alternative LLM, replace accordingly.

df1 = pd.read_csv("data.csv")

agent = Agent(
    [df1],
    config={"verbose": True, "response_parser": StreamlitResponse, "llm": llm},
)

st.title("Pandas-AI demo using climate data")

'''
A simple demo based on Mauna Loa CO2 Records. Ask questions of the data below:
'''

## Dataset
st.dataframe(df1)

## Chatbot
with st.container():
    prompt = st.chat_input("Plot CO2 over time")
    if prompt:
        with st.spinner():
            resp = agent.chat(prompt)
            if os.path.isfile('exports/charts/temp_chart.png'):
                im = plt.imread('exports/charts/temp_chart.png')
                st.image(im)
                os.remove('exports/charts/temp_chart.png')
            st.write(resp)

st.divider()

'''
[pandas-ai docs](https://docs.pandas-ai.com/intro)
Copyright 2024 [Carl Boettiger](https://carlboettiger.info), UC Berkeley.  
License: BSD2
Data from: <https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt>
'''
