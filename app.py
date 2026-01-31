from reports.charts import generate_allocation_pie
from flask import Flask, render_template, request
from config import Config

from services.portfolio import analyze_portfolio
from ai.reasoning import PortfolioAnalyst, PortfolioChatbot

from reports.pdf_report import generate_portfolio_pdf
from flask import send_file

from services.market_data import get_stock_data
from services.indicators import add_technical_indicators
from ai.reasoning import StockAnalyst

from database.db import SessionLocal
from database.models import Portfolio

from reports.charts import generate_stock_price_chart

import dspy

app = Flask(__name__)
app.config.from_object(Config)

# Configure DSPy
lm = dspy.LM(model="openai/gpt-3.5-turbo")
dspy.settings.configure(lm=lm)


@app.route("/")
def home():
    return """
    <h2>AI Financial Analyst Assistant</h2>
    <ul>
        <li><a href='/portfolio'>Portfolio Analysis</a></li>
        <li><a href='/stock'>Single Stock Analysis</a></li>
    </ul>
    """


@app.route("/portfolio", methods=["GET", "POST"])
def portfolio():
    db = SessionLocal()
    chatbot_answer = None

    # ADD STOCK
    if request.method == "POST" and "add_stock" in request.form:
        symbol = request.form.get("symbol").upper()
        quantity = int(request.form.get("quantity"))
        buy_price = float(request.form.get("buy_price"))

        new_stock = Portfolio(
            symbol=symbol,
            quantity=quantity,
            buy_price=buy_price
        )
        db.add(new_stock)
        db.commit()

    # REMOVE STOCK (BY SYMBOL)
    if request.method == "POST" and "remove_stock" in request.form:
        symbol = request.form.get("symbol")
        if symbol:
            db.query(Portfolio).filter(Portfolio.symbol == symbol).delete()
            db.commit()

    # ASK CHATBOT
    if request.method == "POST" and "ask_ai" in request.form:
        user_question = request.form.get("question")

        portfolio_data = analyze_portfolio()
        chatbot = PortfolioChatbot()
        response = chatbot(portfolio_data, user_question)
        chatbot_answer = response.answer

    db.close()

    # Recalculate portfolio
    portfolio_data = analyze_portfolio()
    generate_allocation_pie(portfolio_data)

    analyst = PortfolioAnalyst()
    ai_result = analyst(portfolio_data)

    return render_template(
        "portfolio.html",
        portfolio=portfolio_data,
        analysis=ai_result.analysis,
        chatbot_answer=chatbot_answer
    )

@app.route("/download-report")
def download_report():
    portfolio_data = analyze_portfolio()

    analyst = PortfolioAnalyst()
    ai_result = analyst(portfolio_data)

    pdf_path = generate_portfolio_pdf(
        portfolio_data,
        ai_result.analysis
    )

    return send_file(pdf_path, as_attachment=True)

@app.route("/stock", methods=["GET", "POST"])
def stock_analysis():
    stock_result = None
    ai_analysis = None
    symbol = None   # ✅ needed for chart display

    if request.method == "POST":
        symbol = request.form.get("symbol").upper()

        # Fetch stock data
        data = get_stock_data(symbol, period="6mo")
        data = add_technical_indicators(data)

        # 🔥 Generate price trend line chart
        generate_stock_price_chart(symbol, data)

        # AI analysis
        analyst = StockAnalyst()
        ai_result = analyst(symbol, data.tail(20).to_string())

        stock_result = {
            "symbol": symbol,
            "current_price": round(data["Close"].iloc[-1], 2),
            "ma_20": round(data["MA_20"].iloc[-1], 2),
            "ma_50": round(data["MA_50"].iloc[-1], 2),
            "volatility": round(data["Volatility_20"].iloc[-1], 4)
        }

        ai_analysis = ai_result.analysis

    return render_template(
        "stock.html",
        stock=stock_result,
        analysis=ai_analysis,
        symbol=symbol   # ✅ pass symbol to HTML
    )

if __name__ == "__main__":
    app.run(debug=True)

