import matplotlib.pyplot as plt

def plot_predictions(data, predictions):
    plt.figure(figsize=(12,6))
    plt.plot(data.index, data['Close'], label='Actual Price')
    plt.plot(data.index[-len(predictions):], predictions, label='Predicted Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock Price Prediction')
    plt.legend()
    plt.savefig('stock_prediction.png')
    plt.show()