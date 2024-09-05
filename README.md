# US Census Insurance Data Analysis

This project analyzes insurance data from the US census, focusing on whether smokers pay more in insurance than non-smokers with children. Using SQL and Python, we sort and query data related to smokers, non-smokers, individuals with children, and individuals without children to test our hypothesis.

## Hypothesis

The goal of this project is to determine whether **smokers pay more in insurance than individuals with children**.

## Data Overview

- **Total entries in the dataset**: 1338
- **Average insurance charge**: \$13,270.42

### Caveat: Skewed Averages

While the average charge is \$13,270.42, averages are non-robust statistics, meaning that extremely low or high insurance charges could skew the average. To explore this further, I examined the top and bottom insurance charges.

```python
# Find the top 10 and bottom 10 insurance charges
def find_top_charges():
    query = "SELECT charges FROM US_CENSUS ORDER BY charges DESC LIMIT 10"
    return query_census_data(query)
```
``` python
def find_bottom_charges():
    query = "SELECT charges FROM US_CENSUS ORDER BY charges ASC LIMIT 10"
    return query_census_data(query)
```
Top and Bottom Insurance Charges
The top 5 insurance charges are relatively close together, leading to an expanded range of the top and bottom 10 charges, which still proved unhelpful in understanding the skewness. Therefore, we explored more robust statistics like the interquartile range and standard deviation.

Variability in Insurance Charges
Using interquartile range (IQR) and standard deviation (STD), I found that the variability in insurance charges is high. This suggests that although the average is $13,270, individuals' charges vary significantly from the mean.

Interquartile Range (IQR): $11,899
Standard Deviation (STD): $12,110

```python
def calculate_iqr_and_std():
    charges = get_all_charges()
    q75, q25 = np.percentile(charges, [75, 25])
    iqr = q75 - q25
    std_dev = statistics.stdev(charges)
    return iqr, std_dev
```

Conclusion
The average charge for smokers is much higher than for those with children, despite smokers (274) being a smaller group than individuals with children (764). The analysis shows:

Average insurance cost for smokers: $30,000+
Average insurance cost for non-smoking parents: $9,000+
## Further Exploration
If we extended the analysis, we could examine whether age and BMI also contribute to the higher insurance charges for smokers. However, based on the current scope of the project, the conclusion is that smoking is more expensive than having children in terms of insurance.

This analysis does not account for additional factors like schooling costs for children but strictly focuses on insurance data.

SQL Queries and Python Functions Used
Below are some of the SQL queries and Python functions used to calculate various statistics in this project:

``` python

# Count non-smokers and smokers
def count_non_smokers():
    query = "SELECT COUNT(*) FROM US_CENSUS WHERE LOWER(smoker) = 'no'"
    return query_census_data(query)
```
```python
def count_smokers():
    query = "SELECT COUNT(*) FROM US_CENSUS WHERE LOWER(smoker) = 'yes'"
    return query_census_data(query)
```

# Average charge for smokers with no children
``` python
def average_charge_smokers_no_kids():
    query = "SELECT AVG(charges) FROM US_CENSUS WHERE LOWER(smoker) = 'yes' AND children = 0"
    return query_census_data(query)
```
# Average charge for non-smokers with children
``` python
def average_charge_non_smokers_with_kids():
    query = "SELECT AVG(charges) FROM US_CENSUS WHERE LOWER(smoker) = 'no' AND children > 0"
    return query_census_data(query)

```
This project showcases the power of SQL and Python in analyzing real-world data to test a hypothesis about insurance charges for smokers and non-smokers with children.