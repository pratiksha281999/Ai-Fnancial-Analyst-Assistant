import dspy
from ai.dspy_signatures import PortfolioAnalysisSignature
from ai.dspy_signatures import PortfolioQASignature
from ai.dspy_signatures import StockAnalysisSignature

class PortfolioAnalyst(dspy.Module):
    def __init__(self):
        super().__init__()
        self.analyze = dspy.Predict(PortfolioAnalysisSignature)

    def forward(self, portfolio_data):
        return self.analyze(portfolio_data=portfolio_data)
class PortfolioChatbot(dspy.Module):
    def __init__(self):
        super().__init__()
        self.qa = dspy.Predict(PortfolioQASignature)

    def forward(self, portfolio_data, question):
        return self.qa(
            portfolio_data=portfolio_data,
            question=question
        )

class StockAnalyst(dspy.Module):
    def __init__(self):
        super().__init__()
        self.analyze = dspy.Predict(StockAnalysisSignature)

    def forward(self, symbol, stock_data):
        return self.analyze(
            symbol=symbol,
            stock_data=stock_data
        )
