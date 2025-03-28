import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# QUESTION 1
print("Question 1")
dataset = pd.read_csv('unclean-wine-quality.csv')

dataset.drop(dataset.columns[[0, -1]], axis=1, inplace=True)

nan_indices = np.where(pd.isna(dataset))
print("NaN value indices:", list(zip(nan_indices[0], nan_indices[1])))

total_nans = pd.isna(dataset).sum().sum()
print("Total number of NaNs:", total_nans)

dash_indices = np.where(dataset == '-')
print("Dash value indices:", list(zip(dash_indices[0], dash_indices[1])))

total_dashes = (dataset == '-').sum().sum()
print("Total number of dashes:", total_dashes)

dataset.mask(dataset == '-', other=np.nan, inplace=True)

total_dashes_after = (dataset == '-').sum().sum()
total_nans_after = pd.isna(dataset).sum().sum()
print("Total dashes after replacement:", total_dashes_after)
print("Total NaNs after replacement:", total_nans_after)

dataset = dataset.astype('float64')

# QUESTION 2
print("\nQuestion 2\n")
fill_values = {
    'fixed acidity': 4,
    'volatile acidity': 0,
    'citric acid': 0,
    'residual sugar': 0,
    'chlorides': 1,
    'free sulfur dioxide': 0,
    'total sulfur dioxide': 0,
    'density': 0,
    'pH': 1,
    'sulphates': 1,
    'alcohol': 0
}

dataset.fillna(value=fill_values, inplace=True)

total_nans_after_filling = pd.isna(dataset).sum().sum()
print("Total number of NaNs after filling:", total_nans_after_filling)

print("\nQuestion 3\n")
# QUESTION 3
# Reset dataset by reloading and redoing steps from Q1 (without Q2)
dataset_q3 = pd.read_csv('unclean-wine-quality.csv')
dataset_q3.drop(dataset_q3.columns[[0, -1]], axis=1, inplace=True)
dataset_q3.mask(dataset_q3 == '-', other=np.nan, inplace=True)
dataset_q3 = dataset_q3.astype('float64')

dataset_q3.fillna(method='ffill', inplace=True)

print("Sample-and-hold method:")
print("Value at index [16, 0]:", dataset_q3.iloc[16, 0])
print("Value at index [17, 0]:", dataset_q3.iloc[17, 0])

print("\nQuestion 4\n")
# QUESTION 4
# Reset dataset again for interpolation
dataset_q4 = pd.read_csv('unclean-wine-quality.csv')
dataset_q4.drop(dataset_q4.columns[[0, -1]], axis=1, inplace=True)
dataset_q4.mask(dataset_q4 == '-', other=np.nan, inplace=True)
dataset_q4 = dataset_q4.astype('float64')

dataset_q4.interpolate(method='linear', inplace=True)

print("Linear interpolation method:")
print("Value at index [17, 0]:", dataset_q4.iloc[17, 0])

# Question 5
noisy_sine = pd.read_csv('noisy-sine.csv', header=None)
noisy_sine.columns = ['signal']

window_sizes = [5, 31, 51]
smoothed_signals = {
    f"window_{w}": noisy_sine['signal'].rolling(window=w, center=True).mean()
    for w in window_sizes
}

plt.figure(figsize=(14, 6))
plt.plot(noisy_sine['signal'], label='Original Noisy Signal', alpha=0.6)

for w in window_sizes:
    plt.plot(smoothed_signals[f"window_{w}"], label=f'Moving Avg (window={w})')

plt.title("Moving Average Filtering on Noisy Sine Signal")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Question 6
print("\nQuestion 6\n")

data = pd.read_csv('ECG-sample.csv', header=None, names=['signal'])
plt.figure(figsize=(10, 12))
plt.plot(data['signal'])
plt.title('ECG Signal')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.ylim(0, 1.0)  # Set y-axis limits from 0 to 1.0
plt.show()


def extract_features(signal, window_size=31):
    features = pd.DataFrame(columns=['mean', 'std', 'skewness', 'range'])

    for i in range(len(signal) - window_size + 1):
        window = signal[i:i + window_size]

        # Extract features
        mean = window.mean()
        std = window.std()
        skewness = window.skew()
        range_val = window.max() - window.min()

        # Append to features DataFrame
        features.loc[i] = [mean, std, skewness, range_val]

    return features


features = extract_features(data['signal'])

features_cleaned = features.dropna()

print(features_cleaned)
