# Ai-Fnancial-Analyst-Assistant
AI Financial Analyst Assistant is a Flask-based web application that analyzes stocks and investment portfolios using real-time market data, traditional financial indicators, and AI-driven insights to support informed decision-making.

# Project Overview
- The AI Financial Analyst Assistant is an end-to-end financial analysis web application built using Python and Flask.
- It allows users to analyze individual stocks, manage a stock portfolio, visualize portfolio allocation, and receive AI-generated financial insights through a clean web interface.
- The project focuses on decision support, not stock price guarantees, and demonstrates how AI can be used responsibly to explain financial data.

# Key Features
1) Single Stock Analysis
   - Fetches real-time and historical stock data using Yahoo Finance
   - Calculates technical indicators such as:
       - Moving Averages
       - Volatility
   - Generates structured AI-based stock analysis

2) Portfolio Management
   - Add and remove stocks from a portfolio
   - Stores portfolio data persistently using SQLAlchemy
   - Aggregates holdings and calculates portfolio value
  
3) Portfolio Analytics & Visualization
    - Calculates asset allocation percentages
    - Displays portfolio allocation using a pie chart
    - Highlights diversification and concentration risk

4) AI-Powered Insights & Chatbot
    - Uses structured AI reasoning with DSPy and OpenAI
    - Generates clear, explainable financial insights
    - Allows users to ask questions about their portfolio conversationally
  
5) Automated Reports
    - Generates downloadable PDF portfolio reports
    - Includes portfolio summary, charts, and AI insights
  
# Tech Stack
- Programming Language: Python
- Web Framework: Flask
- Database: SQLite, SQLAlchemy ORM
- AI & NLP: OpenAI API, DSPy
- Data Processing: Pandas, NumPy
- Stock Data API: Yahoo Finance (yfinance)
- Visualization: Matplotlib
- Frontend: HTML, CSS

  
