MLFLOW_TRACKING_URI=http://localhost:5001  mlflow run MLProject_folder --experiment-name='XGBoost_mlflow_validate' -e validate -P X_val=../data/X_val.csv -P y_val=../data/y_val.csv
