# Project 2: Exploratory Data Analysis (EDA)

## Objective
Analyze retail sales data to understand patterns, trends, distributions, relationships, and outliers.

## Dataset
120 retail transactions from January–June 2025 with Order ID, Date, City, Category, Units Sold, Unit Price, Discount, Sales, Payment Method and Customer Rating.

## Tools
Python, Pandas, NumPy, Matplotlib, Excel/VS Code/Jupyter.

## EDA Steps
1. Load and inspect the dataset.
2. Check data types and missing values.
3. Calculate count, mean, median, standard deviation, minimum, maximum and quartiles.
4. Compare sales by product category and city.
5. Analyze monthly sales trends.
6. Study the sales distribution.
7. Detect sales outliers using the IQR method.
8. Examine the relationship between discount and sales.
9. Calculate correlations among numerical variables.

## Key Results
- Total sales: ₹1,443,259.38
- Average order sales: ₹12,027.16
- Median order sales: ₹4,149.50
- Highest-sales category: Electronics
- Highest-sales city: Gurugram
- Highest-sales month: 2025-06
- Potential sales outliers: 17
- Average customer rating: 4.09/5

## Key Observations
- Electronics is the strongest category by total sales.
- Gurugram is the strongest city by total sales.
- Monthly aggregation reveals changes in demand over time.
- A small number of unusually large transactions are detected by the IQR method.
- The discount-versus-sales scatter plot helps assess whether larger discounts are associated with higher sales.
- Customer ratings are generally positive.

## Outlier Method
IQR = Q3 − Q1. Values below Q1 − 1.5×IQR or above Q3 + 1.5×IQR are flagged as potential outliers. They should be investigated rather than automatically deleted.

## Conclusion
EDA converts transaction data into useful business insights. The analysis identifies high-performing categories and cities, monthly trends, sales distributions and unusual transactions. The project can later be extended with sales forecasting, customer segmentation and dashboards.
