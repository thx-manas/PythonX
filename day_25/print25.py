# Day 25: Pandas - The Industry Standard for Data
# Analyzing Eventopia dataset using DataFrames.

import pandas as pd

# 1. Creating a Dataset (Simulating Eventopia data)
data = {
    'Event_Name': ['Devathon', 'Hackathon', 'AstroNight', 'Fintech Summit', 'Code-v-1.0', 'Stargazing'],
    'Department': ['CSE', 'CSE', 'AstroClub', 'Finance', 'CSE', 'AstroClub'],
    'Attendees': [200, 120, 45, 80, 200, 30],
    'Duration_Hrs': [36, 24, 3, 5, 12, 2]
}

# 2. Loading into a DataFrame
df = pd.DataFrame(data)

# 3. ANALYSIS: Quick Data Summary
print("Dataset Overview:")
print(df.describe()) # Statistical summary of numerical columns

# 4. FILTERING: Only show CSE events
cse_events = df[df['Department'] == 'CSE']

# 5. AGGREGATION: Total attendees by Department
total_by_dept = df.groupby('Department')['Attendees'].sum()

print("\n CSE Specific Events:")
print(cse_events)

print("\n Total Engagement per Department:")
print(total_by_dept)