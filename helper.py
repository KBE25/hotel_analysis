import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import statsmodels.api as sm


def compare_models_with_dummies(df, target_col, feature_cols, test_size=0.2, random_state=42):
  """
  Function to compare the fit of different features to explain the target variable. The function was built to take both numerical and
  categorical features by handling the latter with one-hot encoding and performing train-test split.

  Args:
    df: Dataframe containing the data
    target_col: Name of the target column.
    feature_cols: List of feature column names to compare.
    test_size: Proportion of data to use for testing, in this case I am using 20%.
    random_state: Seed for random number generator for reproducibility.

  Returns:
    A dictionary where keys are feature names and values are dictionaries containing model summary statistics (e.g., R-squared, adjusted R-squared, AIC, BIC).
  
  """

  results = {}
  for feature in feature_cols:
    # Select features and target
    X = df[[feature]]
    y = df[target_col]

    # Handle categorical features (if necessary)
    if X.dtypes[feature] == 'object': 
      encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore') 
      X_encoded = pd.DataFrame(encoder.fit_transform(X), columns=encoder.get_feature_names_out([feature]))
      X = X_encoded

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Add constant to the training data
    X_train = sm.add_constant(X_train) 

    # Fit the model on training data
    model = sm.OLS(y_train, X_train).fit()

    # Calculate metrics on training data
    results[feature] = {
        'R-squared': model.rsquared,
        'Adjusted R-squared': model.rsquared_adj,
        'AIC': model.aic,
        'BIC': model.bic
    }

  return results