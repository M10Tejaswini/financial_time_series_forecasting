from .data_loader import load_stock_data
from .model import build_and_train_model
from .predict import make_predictions
from .visualize import plot_predictions

def main():
    ticker = "AAPL"  # Change this to any stock
    data = load_stock_data(ticker)
    model, scaler, X, y = build_and_train_model(data, epochs=10)
    predictions = make_predictions(model, X, scaler)
    plot_predictions(data, predictions)

if __name__ == "__main__":
    main()