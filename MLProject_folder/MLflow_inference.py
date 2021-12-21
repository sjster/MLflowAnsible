import mlflow
import sklearn
from xgboost import XGBClassifier
import pandas as pd
import sys

if __name__ == "__main__":

    mlflow.set_tracking_uri("http://localhost:5001")
    try:
        mlflow.create_experiment('XGBoost_mlflow_training')
        mlflow.set_experiment('XGBoost_mlflow_training')
    except:
        mlflow.set_experiment('XGBoost_mlflow_training')

    X_val = pd.read_csv("../data/X_val.csv")
    y_val = pd.read_csv("../data/y_val.csv")
 
    print("Printing data columns and number of columns")
    print(X_val.columns)
    print(len(X_val.columns))
    print(len(y_val.columns))

    logged_model = 'runs:/005772cea7244bddbfa9a52acff225f8/model'

    with mlflow.start_run(run_name="xgboost_inference") as mlflow_run:
    
        # Load logged model as a sklearn model from run uri
        loaded_model = mlflow.sklearn.load_model(logged_model)

        # Load registerd model as a sklearn model 
        registered_model = mlflow.sklearn.load_model(model_uri=f"models:/xgboost_model/1")

        xgbc_val_metrics = mlflow.sklearn.eval_and_log_metrics(loaded_model, X_val, y_val, prefix="val_")
        print("Using the logged model")
        print(pd.DataFrame(xgbc_val_metrics, index=[0]))

        xgbc_registered_val_metrics = mlflow.sklearn.eval_and_log_metrics(registered_model, X_val, y_val, prefix="val_")
        print("Using the registered model")
        print(pd.DataFrame(xgbc_registered_val_metrics, index=[0]))
        
