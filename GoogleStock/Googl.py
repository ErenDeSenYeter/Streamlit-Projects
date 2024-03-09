# cd Desktop
# streamlit run Googl.py 

import yfinance as yf
import streamlit as st 
import pandas as pd

st.write("""
## Simple Stock Price App
         

Shown are the stock **closing price** and ***volume*** of **Google**
         
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
#ticker symbol defines the which company we are viewing
tickerSymbol = "GOOGL"

#get data on this ticker 
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period="1d",start="2010-5-31",end="2024-1-1")
# Open  High   Low    Close   Volume    Dividens      Stock Splits

st.write("""
## Closing Prices
""")
st.line_chart(tickerDf.Close)


st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)