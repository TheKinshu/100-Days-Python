import pandas as pd

pd.options.display.float_format = '{:,.2f}'.format 

df = pd.read_csv("./Day71/salaries_by_college_major.csv")

# print(df.tail())

clean_df = df.dropna()
# # finds the highest starting salary
# print(clean_df["Starting Median Salary"].max())
# # 
# print(clean_df['Starting Median Salary'].idxmax())
# # Locate the property of index of [x]
# print(clean_df['Undergraduate Major'].loc[43])
# #     clean_df['Undergraduate Major'][43]
# print(clean_df.loc[43])

# Part 1
index = clean_df["Mid-Career Median Salary"].idxmax()
print(clean_df['Undergraduate Major'].loc[index])
minIndex = clean_df["Starting Median Salary"].idxmin()
lowest = clean_df["Undergraduate Major"].loc[minIndex]
print(lowest)
midIndex = clean_df["Mid-Career Median Salary"].idxmin()
lowestMidCareer = clean_df["Undergraduate Major"].loc[midIndex]
print(lowestMidCareer)

spread_col = clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])
clean_df.insert(1, "Spread", spread_col)
#print(clean_df.head())

low_risk = clean_df.sort_values("Spread")
print(low_risk[["Undergraduate Major", "Spread"]].head())

highest_pot = clean_df.sort_values("Mid-Career 90th Percentile Salary",ascending=False)
print(highest_pot[["Undergraduate Major", "Mid-Career 90th Percentile Salary"]].head())

highest_spread = clean_df.sort_values("Spread", ascending=False)
print(highest_spread[["Undergraduate Major", "Spread"]].head())

print(clean_df.groupby('Group').count())
print(clean_df.groupby('Group').mean())