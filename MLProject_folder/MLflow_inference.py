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

    print(X_val.columns)
    print(len(X_val.columns))
    print(len(y_val.columns))

    logged_model = 'runs:/005772cea7244bddbfa9a52acff225f8/model'

    with mlflow.start_run(run_name="xgboost_inference") as mlflow_run:
    
        # Load model as a PyFuncModel.
        loaded_model = mlflow.sklearn.load_model(logged_model)
        xgbc_val_metrics = mlflow.sklearn.eval_and_log_metrics(loaded_model, X_val, y_val,
                                                                    prefix="val_")
        print(pd.DataFrame(xgbc_val_metrics, index=[0]))
