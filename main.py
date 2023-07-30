import yfinance as yf
import pandas as pd
import streamlit as st

st.title("Simple Stocks App")

# Get the stock name from the user
tickersymbol = st.text_input("Enter your stock code:")

# Get the start date and end date from the user
start_date = st.text_input("Enter the start date (YYYY-MM-DD):")
end_date = st.text_input("Enter the end date (YYYY-MM-DD):")
period = st.text_input("Enter your period :1d")

if tickersymbol and start_date and end_date:
    try:
        # Fetch the company name using yfinance
        tickerdata = yf.Ticker(tickersymbol)
        company_name = tickerdata.info['longName']
        st.header(f"Company Name: {company_name}")

        # Fetch stock data using yfinance for the specified period
        tickerdf = tickerdata.history(period=period, start=start_date, end=end_date)
        st.write("Closing Price")
        st.line_chart(tickerdf['Close'])
        st.write("Volume ")
        st.line_chart(tickerdf['Volume'])
    except Exception as e:
        st.write("Error:", e)
