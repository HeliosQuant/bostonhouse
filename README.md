# Boston House Price Prediction

![Boston House Price](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Mobile_Home_in_Saudi_Arabia.JPG/640px-Mobile_Home_in_Saudi_Arabia.JPG)

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model](#model)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview
The **Boston House Price Prediction** project is a machine learning application built to predict house prices in the Boston area based on various factors like the number of rooms, distance to employment centers, crime rate, and more. This project leverages the **Boston Housing Dataset** which is a well-known dataset used for regression analysis.

The goal is to build an efficient predictive model using various machine learning techniques, including data preprocessing, exploratory data analysis (EDA), feature engineering, and model evaluation.

## Features
- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering and Selection
- Model Training (Linear Regression, Decision Trees, Random Forest, etc.)
- Model Evaluation using Metrics like RMSE and R^2
- Hyperparameter Tuning

## Dataset
The dataset used in this project is the **Boston Housing Dataset**, which contains information about houses in Boston and various attributes affecting their prices.

- **Target Variable**: MEDV (Median value of owner-occupied homes in $1000s)
- **Features**: 
  - CRIM: Per capita crime rate by town
  - ZN: Proportion of residential land zoned for lots over 25,000 sq. ft.
  - INDUS: Proportion of non-retail business acres per town
  - CHAS: Charles River dummy variable (1 if tract bounds river; 0 otherwise)
  - NOX: Nitric oxide concentration (parts per 10 million)
  - RM: Average number of rooms per dwelling
  - AGE: Proportion of owner-occupied units built prior to 1940
  - DIS: Weighted distances to five Boston employment centers
  - RAD: Index of accessibility to radial highways
  - TAX: Full-value property tax rate per $10,000
  - PTRATIO: Pupil-teacher ratio by town
  - B: 1000(Bk - 0.63)^2 where Bk is the proportion of Black residents by town
  - LSTAT: Percentage of lower status of the population

You can download the dataset [here](https://www.kaggle.com/datasets/vikrishnan/boston-house-prices).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/HeliosQuant/bostonhouse.git
   cd bostonhouse
