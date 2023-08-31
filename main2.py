# This is a sample Python script.
import copy


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')



import pandas as pd

# Specify the path to your CSV file
csv_file_path = r'C:\mydatascience\datasets\data.csv'  # Use 'r' to indicate a raw string

# Read the CSV file into a DataFrame
data_frame = pd.read_csv(csv_file_path)

# Print the DataFrame
print(data_frame)


# Assume df is your DataFrame
# For example, you have already loaded a CSV file into a DataFrame named df
# df = pd.read_csv("data.csv")

# Print the columns
for column in data_frame.columns:
    print(column)

# Specify the path to your CSV file
csv_file_path = 'data1.csv'  # Use 'r' to indicate a raw string

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Print the DataFrame
print(df)


