
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(data_path, test_size):
    # Load X, Y
    df = pd.read_csv(data_path)
    data = df['PM2.5'].values
    X_data = []
    y_data = []
    for i in range(len(data) - 169):
        X_data.append(data[i:i+168])
        y_data.append(data[i+168])

    # Split with ratio
    # best 10
    X_train, X_valid, y_train, y_valid = train_test_split(
        X_data, np.array(y_data), test_size=test_size, random_state=1024, shuffle=False)

    return X_train, X_valid, y_train, y_valid

