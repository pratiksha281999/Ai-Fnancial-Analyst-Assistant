from collections import defaultdict

from database.db import SessionLocal
from database.models import Portfolio
from services.market_data import get_stock_data


def analyze_portfolio():
    db = SessionLocal()
    holdings = db.query(Portfolio).all()

    aggregated = defaultdict(lambda: {
        "quantity": 0,
        "total_cost": 0
    })

    # Aggregate holdings by symbol
    for stock in holdings:
        aggregated[stock.symbol]["quantity"] += stock.quantity
        aggregated[stock.symbol]["total_cost"] += stock.quantity * stock.buy_price

    portfolio_summary = []
    total_value = 0.0

    for symbol, data in aggregated.items():
        market_data = get_stock_data(symbol, period="1mo")
        current_price = market_data["Close"].iloc[-1]

        quantity = data["quantity"]
        avg_buy_price = round(data["total_cost"] / quantity, 2)
        stock_value = round(current_price * quantity, 2)

        total_value += stock_value

        portfolio_summary.append({
            "symbol": symbol,
            "quantity": quantity,
            "buy_price": avg_buy_price,
            "current_price": round(current_price, 2),
            "value": stock_value
        })

    # Calculate allocation %
    for item in portfolio_summary:
        item["allocation_percent"] = round(
            (item["value"] / total_value) * 100, 2
        )

    db.close()

    return {
        "total_portfolio_value": round(total_value, 2),
        "holdings": portfolio_summary
    }
