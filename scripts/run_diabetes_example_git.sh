MLFLOW_TRACKING_URI=http://localhost:5001  mlflow run https://github.com/sjster/MLflowAnsible#MLProject_folder --experiment-name='Diabetes_experiment'  -e diabetes  -P alpha=0.01 -P l1_ratio=0.01
