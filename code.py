# ----- Cell 1 -----
import pandas as pd
import matplotlib.pyplot as plt
import pingouin
from scipy.stats import mannwhitneyu

# ----- Cell 2 -----
men = pd.read_csv("men_results.csv")
women = pd.read_csv("women_results.csv")

# ----- Cell 3 -----
print(men)

# ----- Cell 4 -----
print(women)

# ----- Cell 5 -----
men["date"] = pd.to_datetime(men["date"])
men_subset = men[(men["date"] > "2002-01-01") & (men["tournament"].isin(["FIFA World Cup"]))]

# ----- Cell 6 -----
print(men_subset)

# ----- Cell 7 -----
women["date"] = pd.to_datetime(women["date"])
women_subset = women[(women["date"] > "2002-01-01") & (women["tournament"].isin(["FIFA World Cup"]))]

# ----- Cell 8 -----
print(women_subset)

# ----- Cell 9 -----
men_subset["group"] = "men"
women_subset["group"] = "women"
men_subset["goals_scored"] = men_subset["home_score"] + men_subset["away_score"]
women_subset["goals_scored"] = women_subset["home_score"] + women_subset["away_score"]

# ----- Cell 10 -----
men_subset["goals_scored"].hist()
plt.show()
plt.clf()

# ----- Cell 11 -----
both = pd.concat([women_subset, men_subset], axis=0, ignore_index=True)

# ----- Cell 12 -----
print(both)

# ----- Cell 13 -----
both_subset = both[["goals_scored", "group"]]
print(both_subset)

# ----- Cell 14 -----
both_subset_wide = both_subset.pivot(columns="group", values="goals_scored")
print(both_subset_wide)

# ----- Cell 15 -----
results_pg = pingouin.mwu(x=both_subset_wide["women"],
                          y=both_subset_wide["men"],
                          alternative="greater")

# ----- Cell 16 -----
print(results_pg)

# ----- Cell 17 -----
results_scipy = mannwhitneyu(x=women_subset["goals_scored"],
                             y=men_subset["goals_scored"],
                             alternative="greater")

# ----- Cell 18 -----
print(results_scipy)

# ----- Cell 19 -----
p_val = results_pg["p-val"].values[0]

# ----- Cell 20 -----
print(p_val)

# ----- Cell 21 -----
if p_val <= 0.01:
    result = "reject"
else:
    result = "fail to reject"

result_dict = {"p_val": p_val, "result": result}

# ----- Cell 22 -----
print(result_dict)

