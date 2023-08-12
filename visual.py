import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

'''visualization of the dataset'''
class Visual:
    def run(self):
        df = self.read_file()
        df = self.filter_df(df)
        print(df)
        self.plot_signal_with_direction(df)
        #self.plot_momentum_signal(df)
        #self.plot_change_signal(df)
        #df = self.filter_change_with_momentum(df)
        #self.plot_change_filtered(df)
        #df = self.filter_test_signal(df)
        #self.plot_test(df)

    def read_file(self):
        filename = 'dataset.csv'
        df = pd.read_csv(filename, names=['receive_timestamp', 'symbol', 'timestamp', \
            'price', 'momentum_signal', 'signal_with_direction', \
            'change_signal'])
        df['receive_timestamp'] = pd.to_datetime(df['receive_timestamp'])
        df.set_index('receive_timestamp', inplace=True)
        return df
    
    def filter_df(self, df, symbol='ETH-USD'):
        df = df.loc[df['symbol'] == symbol]
        return df
    
    def plot_signal_with_direction(self, df):
        fig, ax = plt.subplots()
        colors = {
        0:'grey',
        1:'green',
        -1: 'red'
        }
        ax.scatter(
        np.reshape(df.index,-1),
        np.reshape(df['price'],-1),
        c=np.reshape(df['signal_with_direction'].apply(lambda x: colors[x]),-1),
        s=10,
        linewidths = 1
        )
        plt.show()

    def plot_momentum_signal(self, df):
        fig, ax = plt.subplots()
        colors = {
        0:'grey',
        1:'green',
        2:'red',
        3:'black'
        }
        ax.scatter(
        np.reshape(df.index,-1),
        np.reshape(df['price'],-1),
        c=np.reshape(df['momentum_signal'].apply(lambda x: colors[x]),-1),
        s=10,
        linewidths = 1
        )
        plt.show()
  
    def plot_change_signal(self, df):
        fig, ax = plt.subplots()
        colors = {
        0:'grey',
        1:'green',
        -1: 'red'
        }
        ax.scatter(
        np.reshape(df.index,-1),
        np.reshape(df['price'],-1),
        c=np.reshape(df['change_signal'].apply(lambda x: colors[x]),-1),
        s=10,
        linewidths = 1
        )
        plt.show()

    def filter_change_with_momentum(self, df):
        df['change_filtered'] = df['change_signal'].where(df['momentum_signal'] > 1, 0)
        return df
    
    def plot_change_filtered(self, df):
        fig, ax = plt.subplots()
        colors = {
        0:'grey',
        1:'green',
        -1: 'red'
        }
        ax.scatter(
        np.reshape(df.index,-1),
        np.reshape(df['price'],-1),
        c=np.reshape(df['change_filtered'].apply(lambda x: colors[x]),-1),
        s=10,
        linewidths = 1
        )
        plt.show()
    
    def filter_test_signal(self, df):
        df['test'] = df['signal_with_direction'].where(df['momentum_signal'] > 2, 0)
        df['test'] = df['test'].where(df['test'] == df['change_filtered'], 0)
        return df 
    
    def plot_test(self, df):
        fig, ax = plt.subplots()
        colors = {
        0:'grey',
        1:'green',
        -1: 'red'
        }
        ax.scatter(
        np.reshape(df.index,-1),
        np.reshape(df['price'],-1),
        c=np.reshape(df['test'].apply(lambda x: colors[x]),-1),
        s=10,
        linewidths = 1
        )
        plt.show()
    
            
if __name__ == '__main__':
    v = Visual()
    v.run()
