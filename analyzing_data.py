import pandas as pd
import matplotlib.pyplot as plt

# Loading the Electric Vehicle dataset into pandas Dataframe
df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

# Display the first five rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Display the size of the dataset
print("\nDataset shape (rows, columns):")
print(df.shape)

# Display the column names
print("\nColumn names:")
print(df.columns)

# Cleaning the Dataset Section

# Removing duplicate rows
df = df.drop_duplicates()

# Removing rows with missing important values
df = df.dropna(subset=["County", "Make", "Model Year", "Electric Vehicle Type", "Electric Range"])

# Ensuring that Model Year and Electric Range are numeric
df["Model Year"] = pd.to_numeric(df["Model Year"], errors="coerce")
df["Electric Range"] = pd.to_numeric(df["Electric Range"], errors="coerce")

# Dropping rows that conversion creates missing values
df = df.dropna(subset=["Model Year", "Electric Range"])

# Convert Model Year to Integer
df["Model Year"] = df["Model Year"].astype(int)


# Filtering and Grouping Section

# Filering vehicles by Model year (2015 - present year)
recent_ev = df[df["Model Year"] >= 2015]

# Grouping by Make, to count how many vehicles has each manufacturer made
make_counts = recent_ev.groupby("Make").size().sort_values(ascending=False)

# Grouping by Model Year to count vehicles by the year
year_counts = recent_ev.groupby("Model Year").size()

# Summary Statistics

# total number of recent EV records
total_recent_evs = recent_ev.shape[0]

# Average electric range
average_range = recent_ev["Electric Range"].mean()

print("\nSummary Statistics:")
print(f"Total EV records from 2015 and newer: {total_recent_evs}")
print(f"Average electric range: {average_range:.2f} miles")

print("\nTop 10 EV manufacturers:")
print(make_counts.head(10))

# Viualization 1 Bar chart for the top 10 EV manufacturers

plt.figure(figsize=(10, 6))
make_counts.head(10).plot(kind="bar")
plt.title("Top 10 Electric Vehicle Manufacturers")
plt.xlabel("Manufacturer")
plt.ylabel("Number of Vehicles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Viualization 2 Line chart for EV counts by model year

plt.figure(figsize=(10, 6))
year_counts.plot(kind="line", marker="o")
plt.title("Electric Vehicle Counts by Model Year")
plt.xlabel("Model Year")
plt.ylabel("Number of Vehicles")
plt.grid(True)
plt.tight_layout()
plt.show()