import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv("Superstore.csv", encoding="latin1")

tech = df[df["Category"]=="Technology"]["Profit"]

furniture = df[df["Category"]=="Furniture"]["Profit"]

t_stat, p_value = ttest_ind(tech, furniture)

print("T Statistic:", t_stat)
print("P Value:", p_value)

if p_value < 0.05:
    print("Reject Null Hypothesis")
    print("Technology and Furniture profits differ significantly.")
else:
    print("Fail to Reject Null Hypothesis")
    print("No significant difference found.")