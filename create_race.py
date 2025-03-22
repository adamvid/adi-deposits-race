import pandas as pd
import bar_chart_race as bcr
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('FULLADIDEPOSIT.csv')

# Create a mapping of ABN to Name
abn_to_name = dict(zip(df['ABN'], df['Name']))

# Remove the 'Name' column and set ABN as index
df = df.drop('Name', axis=1).set_index('ABN')

# Transpose the dataframe so dates are the index
df = df.T

# Convert all values to numeric, replacing any errors with NaN
df = df.apply(pd.to_numeric, errors='coerce')

# Convert values to billions (since original data is in millions)
df = df / 1

# Replace ABN with bank names
df.columns = [abn_to_name[abn] for abn in df.columns]

# Sort values for each date to get top 4
df_sorted = df.apply(lambda x: x.sort_values(ascending=False).head(4), axis=1)

# Drop any rows that contain all NaN values
df_sorted = df_sorted.dropna(how='all')

# Sample the data to reduce number of frames (take every nth row)
n = 2  # Adjust this value to get desired frame count
df_sorted = df_sorted.iloc[::n]

# Add a credit frame at the end
last_values = df_sorted.iloc[-1].copy()
credit_frame = pd.DataFrame([last_values], index=['Credits'])
df_final = pd.concat([df_sorted, credit_frame])

# Calculate timing for exactly 30 seconds at 60fps
total_desired_frames = 30 * 60  # 30 seconds * 60fps = 1800 frames
total_periods = len(df_final)
steps_per_period = total_desired_frames // total_periods

# Create the bar chart race
bcr.bar_chart_race(
    df=df_final,
    filename='top_4_ADI.mp4',
    title='Top 4 ADI Deposits ($M)\nDavid Ma 2025 via Cursor AI',
    steps_per_period=steps_per_period,
    period_length=500    # Shorter period length for smoother animation
) 