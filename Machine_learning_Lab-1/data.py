import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import read_csv
def load_boston_data(filepath: str) -> pd.DataFrame:
    coloumn_names = ['CRIM','ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS','RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
    data = read_csv(filepath, header=None, skiprows=22, names =coloumn_names, sep="\s+")
    data_1 = pd.DataFrame(data=data)
    for it in range(len(data_1)-1):
        if np.isnan(data_1["B"][it]):
            data_1.B[it] = data_1.CRIM[it+1]
            data_1.LSTAT[it] = data_1.ZN[it+1]
            data_1.MEDV[it] = data_1.INDUS[it+1]
    data_1 = data_1.dropna()
    data_1.reset_index(drop = True, inplace =True)
    return data_1
data_1 = load_boston_data('boston.csv')
print(data_1.head())