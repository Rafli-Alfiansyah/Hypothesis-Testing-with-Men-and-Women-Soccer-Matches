# Hypothesis Testing with Men's and Women's Soccer Matches

## An Investigation into Goal-Scoring Trends in International Soccer

As a sports journalist specializing in soccer analysis, I've noticed a persistent trend that my gut tells me is worth investigating: it seems that more goals are scored in women's international football matches than in men's. This observation, if statistically validated, would make for a compelling and highly engaging article for our subscribers. To move beyond mere anecdotal evidence and provide a data-driven analysis, I will conduct a formal statistical hypothesis test.

### Scope and Data Collection

To ensure the analysis is both relevant and reliable, I've decided to narrow the scope of the investigation. The sport has evolved significantly over the years, and a simple comparison of all matches would likely be skewed by historical context and a wide variety of tournaments. Therefore, I'm limiting my dataset to **official FIFA World Cup matches** (excluding qualifiers) played since **January 1, 2002**. This focused approach will provide a more accurate comparison of modern-era performance.
The data for this project has been meticulously scraped from a reputable online source and is stored in two CSV files: `women_results.csv` and `men_results.csv`. These datasets contain the results of every official international football match since the 19th century, allowing me to carefully filter for the specific subset of matches required for this analysis.

### Hypothesis Formulation and Statistical Test

The core question I am seeking to answer is whether the mean number of goals scored in women's international soccer matches is greater than in men's. To formally test this, I have established the following null and alternative hypotheses:
**Null Hypothesis ($H_0$)**: The mean number of goals scored in women's international soccer matches is the same as men's.
**Alternative Hypothesis ($H_A$)**: The mean number of goals scored in women's international soccer matches is greater than men's.
For the statistical analysis, I will assume a **10% significance level** ($\alpha = 0.10$). The chosen significance level allows for a degree of flexibility in our analysis, reflecting the inherent variability in sports data while still providing a robust framework for drawing conclusions. By performing a valid statistical test, I aim to either reject the null hypothesis in favor of my alternative hypothesis or conclude that there is not enough evidence to support the claim, thus providing a definitive, data-backed answer to my initial observation. 
