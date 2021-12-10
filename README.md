


### Tracking Server

From ./keras folder start the tracking server

mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 0.0.0.0

### Run the MLflow Project

MLFLOW_TRACKING_URI=http://0.0.0.0:5000 mlflow run MLProject_folder --experiment-name="XGBoost_mlflow_training" -P data_file=../data/WA_Fn-UseC_-Telco-Customer-Churn.csv
