import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("road_traffic_deaths.csv")

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# Plot the data as a line plot
axs[0].plot(df["Year"], df["Fatalities"])
axs[0].set_xlabel("Year")
axs[0].set_ylabel("Fatalities")
axs[0].set_title("Road Traffic Deaths in Ireland from 2000-2023\nSource: The Road Safety Authority")

# Plot the data as a pie chart
axs[1].pie(df["Fatalities"], labels=df["Year"], autopct='%1.1f%%')
axs[1].set_title("\n\nRoad Traffic Deaths Distribution by Year")

plt.tight_layout()
plt.show()
