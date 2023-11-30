# Survival Analysis and Customer Lifetime Value (CLV) Modeling
This repository contains code and analysis for Survival Analysis using Accelerated Failure Time (AFT) models and Customer Lifetime Value (CLV) calculations.

## Overview
The project involves using AFT models to analyze survival patterns and predict customer churn. Additionally, Customer Lifetime Value (CLV) is calculated to estimate the future value of customers.

## Table of Contents
- AFT Models
- Weibull AFT Model
- Log-Normal AFT Model
- Log-Logistic AFT Model
- Model Comparison
- Key Findings

## AFT Models
### Weibull AFT Model
The lambda_ coefficients represent the baseline hazard. Negative values indicate a decrease in hazard. lambda_ ID has a negative coefficient, suggesting that the baseline hazard decreases with ID.
The rho_ coefficient represents the shape parameter of the Weibull distribution. A positive coefficient suggests increasing hazard over time (e.g., 0.183884).
### Log-Normal AFT Model
mu_ (Location Parameter): Positive coefficients indicate an increase in the location parameter, implying higher hazard (e.g., -0.000474).
sigma_ (Scale Parameter): Represents the standard deviation of the log-normal distribution. A higher value suggests higher variability in survival times.
### Log-Logistic AFT Model
alpha_ (Shape Parameter): Positive coefficient implies increasing hazard over time, while a negative coefficient suggests decreasing hazard (e.g., -0.000466).
beta_ (Scale Parameter): Reflects the degree of variability in survival times.

## Model Comparison
"custcat_E-service," "custcat_Plus service," and "custcat_Total service" have significant positive coefficients in all models, suggesting a higher hazard for these customer categories.
"income" has a small but positive coefficient in Weibull and log-normal models, indicating a slight increase in hazard with income.

## Key Findings
From our plot, the LogNormal model has the lowest AIC and BIC, and the highest log-likelihood value. This means that the model fits better than the others to our data. So, we choose the LogNormal model as our AFT Fitter.

The significant features are: address, age, custcat_E-service, custcat_Plus service, custcat_Total service, internet_Yes, marital_Unmarried, voice_Yes, according to their p-values.


```python

```


```python

```
