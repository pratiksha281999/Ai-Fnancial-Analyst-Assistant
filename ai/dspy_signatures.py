import dspy


class PortfolioAnalysisSignature(dspy.Signature):
    """
    AI analyzes portfolio data and provides structured insights.
    """

    portfolio_data = dspy.InputField(
        desc="Portfolio summary including holdings, allocation, prices"
    )

    analysis = dspy.OutputField(
        desc=(
            "Provide analysis using plain text only.\n"
            "Use clear section titles WITHOUT markdown symbols.\n"
            "Format like this:\n\n"
            "Portfolio Overview:\n"
            "- point\n\n"
            "Performance Insights:\n"
            "- point\n\n"
            "Risk & Concentration:\n"
            "- point\n\n"
            "Recommendations:\n"
            "- point\n"
        )
    )


class PortfolioQASignature(dspy.Signature):
    """
    AI answers user questions using portfolio context.
    """

    portfolio_data = dspy.InputField(
        desc="User portfolio summary with holdings, allocation, prices"
    )

    question = dspy.InputField(
        desc="User's question about their portfolio"
    )

    answer = dspy.OutputField(
        desc=(
            "Answer clearly and professionally in plain text.\n"
            "Base the response only on the given portfolio data.\n"
            "Give actionable financial guidance."
        )
    )


class StockAnalysisSignature(dspy.Signature):
    """
    AI analyzes a single stock using market data.
    """

    stock_data = dspy.InputField(
        desc="Recent stock price data with indicators"
    )

    symbol = dspy.InputField(
        desc="Stock symbol"
    )

    analysis = dspy.OutputField(
        desc=(
            "Provide analysis in plain text ONLY.\n"
            "Use the following structure exactly:\n\n"
            "Overview:\n"
            "- bullet point\n\n"
            "Trend:\n"
            "- bullet point\n\n"
            "Risk:\n"
            "- bullet point\n\n"
            "Recommendation:\n"
            "- bullet point\n\n"
            "Use short bullet points.\n"
            "Do NOT write paragraphs.\n"
            "Do NOT use markdown symbols like ** or ##."
        )
    )
