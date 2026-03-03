import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("airplane_crashes.csv")

# 1. Convert Time to datetime and extract the hour
# We use errors='coerce' to turn invalid times into NaT (Not a Time)
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M', errors='coerce').dt.hour

# 2. Drop rows where time couldn't be parsed
df = df.dropna(subset=['Time'])

# 3. Categorize into Time of Day
# Bins: 0-5 (Night), 5-12 (Morning), 12-17 (Afternoon), 17-21 (Evening), 21-24 (Night)
bins = [0, 5, 12, 17, 21, 24]
labels = ['Night', 'Morning', 'Afternoon', 'Evening', 'Night']

# Note: We use 'ordered=False' because Night appears twice in the labels logic
df['Time_of_Day'] = pd.cut(df['Time'], bins=bins, labels=labels, right=False, include_lowest=True, ordered=False)

# 4. Count the results
counts = df['Time_of_Day'].value_counts()
print("Crash counts by time of day:")
print(counts)

# 5. Identify the riskiest period
riskiest = counts.idxmax()
print(f"\nThe riskiest period is: {riskiest}")

# 6. Visualize
counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Number of Crashes by Time of Day')
plt.xlabel('Time Period')
plt.ylabel('Number of Crashes')
plt.xticks(rotation=45)
plt.show()