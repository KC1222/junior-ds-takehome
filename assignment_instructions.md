# Assignment Tasks

Please complete the following steps in a Jupyter Notebook or a Python script.

### Part 1: Data Cleaning & Feature Engineering (Pandas)
Using the `delivery_data.csv` you generated.
1. **Handle Erronous Values:** Identify missing values in `driver_rating` and impute them with the median rating.
2. **Feature Extraction:** The dataset has a `timestamp` column. Create two new features that might benefit the regression problem.


### Part 2: Pipeline Construction
We want to verify your ability to prevent data leakage and write clean modeling code.
Build a `sklearn.pipeline.Pipeline` that includes preprocessing and a Regression Model of your choice.

### Part 3: Evaluation
1. Train the pipeline on the training set.
2. Predict on the test set.
3. Calculate and print accuracy metrics.
4. **Bonus (Optional):** Plot the "Actual vs Predicted" delivery times using a plotting tool of your choice.

### Part 4: Short Answers
Please include a README.md file with your answers to the following questions.

1. You might have noticed rows with negative package weights. If you found that 25% of the dataset had negative weights, would you drop them? If not, what would you do instead?
2. Imagine the traffic_level data comes from a paid API that costs us money every time we call it. How would you determine if this feature is 'worth' the cost?