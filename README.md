# Hypothesis Testing with Men's and Women's Soccer Matches

![soccer-pitch](https://github.com/user-attachments/assets/6d0151d4-dfaf-478a-aadb-144ee54afc37)

## An Investigation into Goal-Scoring Trends in International Soccer

I've noticed a persistent trend that this is worth investigating: it seems that more goals are scored in women's international football matches than in men's. This observation, if statistically validated, would make for a compelling and highly engaging article for our subscribers. To move beyond mere anecdotal evidence and provide a data-driven analysis, I will conduct a formal statistical hypothesis test.

### Scope and Data Collection

To ensure the analysis is both relevant and reliable, I've decided to narrow the scope of the investigation. The sport has evolved significantly over the years, and a simple comparison of all matches would likely be skewed by historical context and a wide variety of tournaments. Therefore, I'm limiting my dataset to **official FIFA World Cup matches** (excluding qualifiers) played since **January 1, 2002**. This focused approach will provide a more accurate comparison of modern-era performance.
The data for this project has been meticulously scraped from a reputable online source and is stored in two CSV files: `women_results.csv` and `men_results.csv`. These datasets contain the results of every official international football match since the 19th century, allowing me to carefully filter for the specific subset of matches required for this analysis.

### Hypothesis Formulation and Statistical Test

The core question I am seeking to answer is whether the mean number of goals scored in women's international soccer matches is greater than in men's. To formally test this, I have established the following null and alternative hypotheses:
**Null Hypothesis ($H_0$)**: The mean number of goals scored in women's international soccer matches is the same as men's.
**Alternative Hypothesis ($H_A$)**: The mean number of goals scored in women's international soccer matches is greater than men's.
For the statistical analysis, I will assume a **10% significance level** ($\alpha = 0.10$). The chosen significance level allows for a degree of flexibility in our analysis, reflecting the inherent variability in sports data while still providing a robust framework for drawing conclusions. By performing a valid statistical test, I aim to either reject the null hypothesis in favor of my alternative hypothesis or conclude that there is not enough evidence to support the claim, thus providing a definitive, data-backed answer to my initial observation. 

### Results

The analysis began by filtering the datasets to isolate FIFA World Cup matches played since January 1, 2002. This resulted in a sample of **200 women's matches** and **384 men's matches**. For each match, the total number of goals was calculated by summing the home and away scores.
To test the hypothesis, a **Mann-Whitney U test** was performed. This non-parametric test was chosen to compare the distributions of goals scored between the men's and women's matches. The test was specifically configured to check if the number of goals in women's matches was statistically "greater" than in men's matches.
The test yielded a **p-value of approximately 0.0051**.

### Conclusion

The core of hypothesis testing is to compare the calculated p-value against a predetermined significance level (α). In this investigation, the significance level was set at **0.10**.
Our resulting p-value (0.0051) is significantly lower than the alpha value (0.10). Therefore, we **reject the null hypothesis**.
This indicates a statistically significant result. The data provides strong evidence to support the alternative hypothesis, leading to the conclusion that, within the scope of FIFA World Cup matches since 2002, **more goals are scored in women's matches than in men's matches**.

### Tools

- **Python**
