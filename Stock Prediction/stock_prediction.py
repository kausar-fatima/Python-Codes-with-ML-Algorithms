# LSTM (Long Short-Term Memory) neural networks Algorithm
import pandas as pd  # for data manupilation
import numpy as np  # for numerical operations
import matplotlib.pyplot as plt  # for plotting
from sklearn.preprocessing import MinMaxScaler  # for data scalling
from sklearn.metrics import mean_squared_error  # mean_squared_error for evaluation
from keras.models import Sequential # for building and training a neural network
from keras.layers import LSTM, Dense
import tkinter as tk  # for creating a simple GUI application
from tkinter import ttk
from tkinter import filedialog

class StockPredictionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Prediction App")
        # label is positioned in the first row and first column of the grid layout.
        self.select_label = ttk.Label(self.root, text="Select Stock:")
        self.select_label.grid(row=0, column=0, padx=10, pady=10)

        self.stock_var = tk.StringVar()
        self.stock_combobox = ttk.Combobox(self.root, textvariable=self.stock_var, values=[
            'AAPL', 'AXP', 'BA', 'CAT', 'CSCO', 'CVX', 'DIS', 'DWDP', 'GE', 'GS', 'HD', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO',
            'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PFE', 'PG', 'TRV', 'UNH', 'UTX', 'V', 'VZ', 'WMT', 'XOM'])
        self.stock_combobox.grid(row=0, column=1, padx=10, pady=10)

        # associated with the plot_forecast method to be called when the button is clicked
        self.plot_button = ttk.Button(self.root, text="Plot Forecast", command=self.plot_forecast)
        self.plot_button.grid(row=1, column=0, columnspan=2, pady=10)

        # root mean square error (RMSE) 
        self.rmse_label = ttk.Label(self.root, text="RMSE values:")
        self.rmse_label.grid(row=2, column=0, columnspan=2, pady=10)

    def plot_forecast(self):
        selected_stock = self.stock_var.get()
        if not selected_stock:
            tk.messagebox.showinfo("Error", "Please select a stock.")
            return

        df = pd.read_csv(f'data/{selected_stock}.csv')
        #  extracts the values from the second-to-last column
        data = df.iloc[:, -2].values

        # data by scaling, splitting it into training and testing sets, and creating an LSTM model
        n_lag = 1
        n_seq = 15
        n_test = 15

        scaler, train, test = self.prepare_data(data, n_test, n_lag, n_seq)
        model = self.build_lstm_model(n_lag, n_seq)
        self.train_lstm_model(model, train, n_lag, n_seq)

        forecasts = self.make_forecasts_lstm(model, test, n_lag, n_seq, scaler)

        self.evaluate_forecasts(test, forecasts, n_lag, n_seq, scaler)

        self.plot_forecasts(data, forecasts, n_test + 2)

    @staticmethod
    def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
        n_vars = 1 if type(data) is list else data.shape[1]
        df = pd.DataFrame(data)
        cols, names = list(), list()

        for i in range(n_in, 0, -1):
            cols.append(df.shift(i))
            names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]

        for i in range(0, n_out):
            cols.append(df.shift(-i))
            if i == 0:
                names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
            else:
                names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]

        agg = pd.concat(cols, axis=1)
        agg.columns = names

        if dropnan:
            agg.dropna(inplace=True)
        return agg

    @staticmethod
    def prepare_data(series, n_test, n_lag, n_seq):
        raw_values = series.reshape(len(series), 1)
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled = scaler.fit_transform(raw_values)
        supervised = StockPredictionApp.series_to_supervised(scaled, n_lag, n_seq)
        supervised_values = supervised.values
        train, test = supervised_values[0:-n_test], supervised_values[-n_test:]

        return scaler, train, test

    @staticmethod
    def build_lstm_model(n_lag, n_seq):
        model = Sequential()
        model.add(LSTM(50, activation='relu', input_shape=(n_lag, 1)))
        model.add(Dense(n_seq))
        model.compile(optimizer='adam', loss='mse')
        return model

    @staticmethod
    def train_lstm_model(model, train, n_lag, n_seq, epochs=50, batch_size=32):
        X, y = train[:, :n_lag], train[:, n_lag:]
        X = X.reshape((X.shape[0], n_lag, 1))
        model.fit(X, y, epochs=epochs, batch_size=batch_size, verbose=0)

    @staticmethod
    def make_forecasts_lstm(model, test, n_lag, n_seq, scaler):
        forecasts = list()
        for i in range(len(test)):
            X = test[i, :n_lag]
            X = X.reshape((1, n_lag, 1))
            # make forecast
            forecast = model.predict(X, batch_size=1)
            # inverse transform
            forecast = scaler.inverse_transform(forecast)
            forecasts.append(forecast.flatten())
        return forecasts

    def evaluate_forecasts(self, test, forecasts, n_lag, n_seq, scaler):
        rmse_values = []
        for i in range(n_seq):
            actual = test[:, (n_lag + i)]
            predicted = [forecast[i] for forecast in forecasts]
            # inverse transform
            actual = scaler.inverse_transform(actual.reshape(-1, 1))
            rmse = np.sqrt(mean_squared_error(actual, predicted))
            rmse_values.append(rmse)

        # Update the RMSE label on the UI
        self.rmse_label.config(text="RMSE values: " + ", ".join([f"{i+1}: {rmse:.4f}" for i, rmse in enumerate(rmse_values)]))

    @staticmethod
    def plot_forecasts(series, forecasts, n_test):
        # plot the entire dataset in blue
        plt.plot(series, label='Actual Stock Prices')  # Add label for the blue line
        # plot the forecasts in red
        for i in range(len(forecasts)):
           off_s = len(series) - n_test + i - 1
           off_e = off_s + len(forecasts[i]) + 1
           xaxis = [x for x in range(off_s, off_e)]
           yaxis = [series[off_s]] + forecasts[i].tolist()
           plt.plot(xaxis, yaxis, color='red', label=f'Forecast {i+1}')  # Add label for each red line

        # Add axis labels and legend
        plt.xlabel('Time')
        plt.ylabel('Stock Prices')
        plt.legend()

        # show the plot
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = StockPredictionApp(root)
    root.mainloop()
