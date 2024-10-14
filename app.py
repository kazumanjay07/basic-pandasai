import os
import pandas as pd
import streamlit as st
from pandasai import Agent
from pandasai.responses.streamlit_response import StreamlitResponse
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("supermarket_sales - Sheet1.csv")
df = df[['Invoice ID', 'Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Unit price', 'Quantity', 'Tax 5%', 'Total', 'Date', 'Time', 'Payment', 'cogs', 'gross margin percentage', 'gross income', 'Rating']]

# Set the API key
os.environ["PANDASAI_API_KEY"] = "YOUR_API_KEY"

# Create an agent
agent = Agent(df)

# Streamlit interface
st.title("Supermarket Sales Data Query")

st.write("""
A simple interface to ask questions about the supermarket sales data.
""")

# Display the dataframe
st.dataframe(df)

# User input for queries
user_prompt = st.text_input("Enter your question about the data:")

if user_prompt:
    with st.spinner("Getting response..."):
        # Get the response from the agent
        response = agent.chat(user_prompt)
        
        # Print the response to the terminal
        print("Response:", response)
        
        # Check if the response is an image path
        if isinstance(response, str) and os.path.isfile(response):
            # If the response is a valid file path, display the image
            st.image(response, caption="Generated Chart", use_column_width=True)
        else:
            # Display the text response in the Streamlit app
            st.write("Response:", response)

st.divider()

st.write("by Aiman Kamarudin&copy;2024")
