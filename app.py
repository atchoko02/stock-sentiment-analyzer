import streamlit as st
from data import reddit_scraper as scraper
from data import stock_data as stock
from sentiment import analyzer
import pandas as pd
from visualization import graphs

ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA):", "AAPL")
company_name = st.text_input("Enter Company Name:", "Apple Inc.")
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

if st.button("Analyze"):
    posts = scraper.fetch_reddit_posts(ticker, company_name)
    sentiment_df = analyzer.analyze_sentiment(posts)
    stock_df = stock.fetch_stock_data(ticker, start_date, end_date)

    merged_df = pd.merge(sentiment_df, stock_df, on='Date', how='outer')
    
    #Time-series sentiment + stock
    fig1 = graphs.plot_sentiment_vs_stock(merged_df)
    st.plotly_chart(fig1, use_container_width=True)

    #SEntiment distribution
    fig2 = graphs.plot_sentiment_distribution(sentiment_df)
    st.plotly_chart(fig2, use_container_width=True)